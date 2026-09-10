#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <HTTPClient.h>
#include <Wire.h>

#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_PN532.h>

// ═════════════════════════════════════════════
// CREDENCIAIS
// ═════════════════════════════════════════════
const char* WIFI_SSID_PRIMARY = "FamiliaMarques";
const char* WIFI_PASS_PRIMARY = "3202354@Id";

const char* WIFI_SSID_FALLBACK = "iPhone de Wagner";
const char* WIFI_PASS_FALLBACK = "wagner1998";

const char* WIFI_SSID_FALLBACK2 = "WM 14 ProMax";
const char* WIFI_PASS_FALLBACK2 = "12345678";

const char* CLOUDFLARE_HOST = "nfc.softset.workers.dev";
const char* NFC_DEVICE_ID = "softset-voice-01";
const char* DEVICE_TOKEN = "3202354@Id";
const char* NFC_API_PATH = "/api/nfc/read";

// ═════════════════════════════════════════════
// I2C & HARDWARE
// ═════════════════════════════════════════════
#define I2C_SDA 21
#define I2C_SCL 22

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
#define OLED_ADDRESS 0x3C

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
bool oledOK = false;

#define PN532_IRQ_DUMMY 16
#define PN532_RESET_DUMMY 17
Adafruit_PN532 nfc(PN532_IRQ_DUMMY, PN532_RESET_DUMMY, &Wire);

// ═════════════════════════════════════════════
// PRESENÇA NFC (ESTÁVEL E PRECISO)
// ═════════════════════════════════════════════
String activeUID = "";
unsigned long lastSeenMs = 0;
bool presenceSent = false;

const uint16_t NFC_READ_TIMEOUT_MS = 150;
const unsigned long REMOVAL_GRACE_MS = 2000;

const unsigned long WIFI_CHECK_MS = 1000;
unsigned long lastWifiCheckMs = 0;

// ═════════════════════════════════════════════
// UTIL
// ═════════════════════════════════════════════
String uidToString(uint8_t* uid, uint8_t uidLength) {
  String s = "";
  for (uint8_t i = 0; i < uidLength; i++) {
    if (uid[i] < 0x10) s += "0";
    s += String(uid[i], HEX);
    if (i < uidLength - 1) s += ":";
  }
  s.toUpperCase();
  return s;
}

String jsonEscape(String v) {
  v.replace("\\", "\\\\");
  v.replace("\"", "\\\"");
  return v;
}

String jsonField(const String& json, const String& key) {
  String needle = "\"" + key + "\"";
  int k = json.indexOf(needle);
  if (k < 0) return "";
  int colon = json.indexOf(':', k + needle.length());
  if (colon < 0) return "";
  int q1 = json.indexOf('"', colon + 1);
  if (q1 < 0) return "";
  int q2 = q1 + 1;
  while (q2 < json.length()) {
    if (json[q2] == '"' && json[q2 - 1] != '\\') break;
    q2++;
  }
  if (q2 >= json.length()) return "";
  return json.substring(q1 + 1, q2);
}

void showScreen(const String& title, const String& line1 = "", const String& line2 = "") {
  if (!oledOK) return;
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);
  display.setCursor(4, 4);
  display.println(title);
  display.drawLine(0, 15, 127, 15, SSD1306_WHITE);
  display.setCursor(4, 27);
  display.println(line1);
  if (line2.length()) {
    display.setCursor(4, 44);
    display.println(line2);
  }
  display.display();
}

String wifiQualityLabel(int32_t rssi) {
  if (rssi >= -60) return "OTIMA";
  if (rssi >= -70) return "BOA";
  return "FRACA";
}

void showIdle() {
  if (!oledOK) return;
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);
  display.setCursor(16, 3);
  display.println("CONTROLE CRACHAS");
  display.drawLine(0, 15, 127, 15, SSD1306_WHITE);
  display.setCursor(8, 27);
  display.println("PRONTO P/ LER SLOT");
  display.setCursor(2, 55);

  if (WiFi.status() == WL_CONNECTED) {
    int32_t rssi = WiFi.RSSI();
    display.print("WiFi: ");
    display.print(wifiQualityLabel(rssi));
    display.print(" ");
    display.print(rssi);
    display.print("dBm");
  } else {
    display.print("WiFi: OFF");
  }
  display.display();
}

void showWorkerResponse(const String& response, const String& presence) {
  if (response.indexOf("\"registered\":false") >= 0) {
    showScreen("NAO CADASTRADO", jsonField(response, "uid"), "Cadastre no portal");
    return;
  }
  String name = jsonField(response, "person_name");
  String slot = jsonField(response, "slot");
  if (presence == "PRESENT") {
    showScreen(name.length() ? name : "CRACHA", "PAINEL", slot.length() ? "Slot " + slot : "");
  } else {
    showScreen(name.length() ? name : "CRACHA", "EM USO", slot.length() ? "Slot " + slot : "");
  }
}

// ═════════════════════════════════════════════
// WIFI
// ═════════════════════════════════════════════
const unsigned long WIFI_CONNECT_TIMEOUT_MS = 6000;

bool tryWiFi(const char* ssid, const char* password) {
  Serial.print("Tentando WiFi: ");
  Serial.println(ssid);
  showScreen("WIFI", "Conectando...", ssid);

  WiFi.disconnect(false, false);
  delay(100);
  WiFi.begin(ssid, password);

  unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - start < WIFI_CONNECT_TIMEOUT_MS) {
    delay(100);
    Serial.print(".");
  }
  Serial.println();

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("WiFi conectado com sucesso.");
    showScreen("WIFI OK", WiFi.SSID(), WiFi.localIP().toString());
    delay(1500);
    return true;
  }
  return false;
}

void connectWiFi() {
  if (WiFi.status() == WL_CONNECTED) return;
  WiFi.mode(WIFI_STA);
  WiFi.setAutoReconnect(true);
  WiFi.persistent(false);

  if (tryWiFi(WIFI_SSID_PRIMARY, WIFI_PASS_PRIMARY)) return;
  if (tryWiFi(WIFI_SSID_FALLBACK, WIFI_PASS_FALLBACK)) return;
  if (tryWiFi(WIFI_SSID_FALLBACK2, WIFI_PASS_FALLBACK2)) return;

  showScreen("SEM WIFI", "3 redes OFF", "Tentara novamente");
}

void ensureWiFi() {
  if (WiFi.status() == WL_CONNECTED) return;
  if (millis() - lastWifiCheckMs < WIFI_CHECK_MS) return;
  lastWifiCheckMs = millis();
  connectWiFi();
}

// ═════════════════════════════════════════════
// ENVIO HTTPS
// ═════════════════════════════════════════════
bool sendPresence(const String& uid, const String& presence) {
  if (WiFi.status() != WL_CONNECTED) return false;

  WiFiClientSecure client;
  client.setInsecure();
  client.setTimeout(5000);

  HTTPClient https;
  String url = String("https://") + CLOUDFLARE_HOST + NFC_API_PATH;

  if (!https.begin(client, url)) return false;

  https.setTimeout(5000);
  https.addHeader("Content-Type", "application/json");
  https.addHeader("Authorization", String("Bearer ") + DEVICE_TOKEN);
  https.addHeader("X-Device-ID", NFC_DEVICE_ID);

  String payload = "{";
  payload += "\"device_id\":\"" + jsonEscape(String(NFC_DEVICE_ID)) + "\",";
  payload += "\"uid\":\"" + jsonEscape(uid) + "\",";
  payload += "\"presence\":\"" + presence + "\",";
  payload += "\"reader\":\"pn532\",";
  payload += "\"transport\":\"i2c\"";
  payload += "}";

  Serial.print("POST presence=");
  Serial.print(presence);
  Serial.print(" UID=");
  Serial.println(uid);

  int code = https.POST(payload);
  String response = code > 0 ? https.getString() : "";

  Serial.print("HTTP ");
  Serial.println(code);

  if (code >= 200 && code < 300) {
    showWorkerResponse(response, presence);
    https.end();
    return true;
  }

  showScreen("ERRO API", "HTTP " + String(code));
  https.end();
  return false;
}

// ═════════════════════════════════════════════
// SETUP
// ═════════════════════════════════════════════
void setup() {
  Serial.begin(115200);
  delay(800);

  Wire.begin(I2C_SDA, I2C_SCL);
  Wire.setClock(100000);

  oledOK = display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDRESS);
  if (oledOK) showScreen("INICIALIZANDO", "OLED OK");

  connectWiFi();

  if (!nfc.begin()) {
    showScreen("ERRO", "PN532 begin");
    while (true) delay(1000);
  }

  uint32_t versiondata = nfc.getFirmwareVersion();
  if (!versiondata) {
    showScreen("ERRO", "PN532 nao achado");
    while (true) delay(1000);
  }

  if (!nfc.SAMConfig()) {
    showScreen("ERRO", "SAMConfig");
    while (true) delay(1000);
  }

  Serial.println("PN532 Pronto para leitura continua.");
  showIdle();
}

// ═════════════════════════════════════════════
// LOOP (LEITURA RF CONFIÁVEL E TEMPO REAL)
// ═════════════════════════════════════════════
void loop() {
  ensureWiFi();

  uint8_t uid[7] = {0};
  uint8_t uidLength = 0;

  bool found = nfc.readPassiveTargetID(
    PN532_MIFARE_ISO14443A,
    uid,
    &uidLength,
    NFC_READ_TIMEOUT_MS
  );

  if (found && uidLength > 0) {
    String uidString = uidToString(uid, uidLength);
    unsigned long nowMs = millis();

    // 1. Primeira vez que detectou o crachá
    if (activeUID.length() == 0) {
      activeUID = uidString;
      presenceSent = sendPresence(activeUID, "PRESENT");
      lastSeenMs = millis();
      return;
    }

    // 2. O mesmo crachá continua no leitor
    if (uidString == activeUID) {
      lastSeenMs = millis();
      if (!presenceSent && WiFi.status() == WL_CONNECTED) {
        presenceSent = sendPresence(activeUID, "PRESENT");
        lastSeenMs = millis();
      }
      return;
    }

    // 3. Crachá trocou
    sendPresence(activeUID, "REMOVED");
    activeUID = uidString;
    presenceSent = sendPresence(activeUID, "PRESENT");
    lastSeenMs = millis();
    return;
  }

  // 4. Crachá retirado (após 2 segundos reais sem nenhuma leitura de RF)
  if (activeUID.length() > 0 && millis() - lastSeenMs >= REMOVAL_GRACE_MS) {
    String removedUID = activeUID;

    activeUID = "";
    lastSeenMs = 0;
    presenceSent = false;

    Serial.print("CRACHA REMOVIDO: ");
    Serial.println(removedUID);

    sendPresence(removedUID, "REMOVED");

    delay(300);
    showIdle();
  }

  delay(20);
}
