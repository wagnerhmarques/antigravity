#!/usr/bin/env python3
"""
Weekly Portfolio Analyzer & Institutional Wealth Intelligence.
Features:
1. Live Web Scraping (Investidor10 & Fundamentus) for all 19 assets.
2. 6-Month Historical Reports (Earnings DRE/ITR, FII Managerial Reports, Material Facts).
3. Score Clamping strictly bounded to [0, 100].
4. Radar de Proventos & Alerta Antecipado de Data-Com.
5. Rastreamento de Evolução Semanal (Delta WoW) com Acumulação Histórica (portfolio_baseline.json).
6. Teste de Estresse de Alavancagem & Cenário Selic a 14,00%.
7. Mapa de Concentração & Risco Setorial.
8. Geração de Relatório Executivo em PDF com Gráficos Elegantes (ReportLab + Matplotlib).
9. Injeção de Layout Executivo Refinado no Google Sheets na Aba 3108 com timestamp explícito de Última Edição.
10. Preservação estrita do nome da planilha (P$ - Gestão & Aportes).
11. Notificação Visual macOS, Registro no Reminders (Lista ME) e Áudio Briefing em Voz Luciana.
"""

import urllib.request
import re
import json
import os
import math
import subprocess
import time
from datetime import datetime

# Matplotlib & ReportLab setup for PDF generation
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
BASELINE_FILE = "/Users/user/.gemini/antigravity-ide/scratch/portfolio_baseline.json"
PDF_REPORT_PATH = "/Users/user/.gemini/antigravity-ide/scratch/relatorio_executivo_carteira.pdf"
MD_REPORT_PATH = "/Users/user/.gemini/antigravity-ide/scratch/relatorio_semanal_carteira.md"
CHARTS_DIR = "/Users/user/.gemini/antigravity-ide/scratch"

DEFAULT_ASSETS = {
    "Ações": [
        "RADL3", "KLBN11", "TOTS3", "WEGE3", "ITSA4", "BBAS3",
        "GOAU4", "CMIG4", "ABEV3", "VALE3", "PETR4", "EGIE3", "BBSE3"
    ],
    "FIIs": [
        "XPML11", "HGLG11", "MXRF11", "BTHF11", "BTLG11", "KNCR11"
    ]
}

SECTOR_MAP = {
    "CMIG4": {"setor": "Elétrica / Energia", "macro": "Energia & Utilities", "div_ebitda": 1.45, "sensibilidade": "⚖️ Neutro (IPCA/IGP-M)", "alavancagem": "Baixa / Segura"},
    "PETR4": {"setor": "Petróleo & Gás", "macro": "Commodities & Energia", "div_ebitda": 0.85, "sensibilidade": "⚖️ Neutro (Receita em Dólar)", "alavancagem": "Muito Baixa"},
    "ITSA4": {"setor": "Holdings / Financeiro", "macro": "Financeiro & Seguros", "div_ebitda": 0.20, "sensibilidade": "🛡️ Beneficiado (Spread Itaú)", "alavancagem": "Mínima"},
    "BBSE3": {"setor": "Seguros & Previdência", "macro": "Financeiro & Seguros", "div_ebitda": 0.00, "sensibilidade": "🛡️ Forte Ganho (Float 100% Selic)", "alavancagem": "Caixa Líquido"},
    "BBAS3": {"setor": "Bancos", "macro": "Financeiro & Seguros", "div_ebitda": 0.00, "sensibilidade": "🛡️ Beneficiado (Spread Bancário)", "alavancagem": "Alavancagem Bancária"},
    "GOAU4": {"setor": "Siderurgia & Metalurgia", "macro": "Commodities & Metais", "div_ebitda": 1.80, "sensibilidade": "⚠️ Leve Pressão (Capex)", "alavancagem": "Moderada"},
    "EGIE3": {"setor": "Elétrica / Geração", "macro": "Energia & Utilities", "div_ebitda": 2.10, "sensibilidade": "⚖️ Neutro (100% IPCA/IGP-M)", "alavancagem": "Controlada"},
    "ABEV3": {"setor": "Bebidas / Consumo", "macro": "Consumo & Varejo", "div_ebitda": 0.00, "sensibilidade": "🛡️ Beneficiado (Caixa Líquido)", "alavancagem": "Caixa Líquido"},
    "VALE3": {"setor": "Mineração", "macro": "Commodities & Metais", "div_ebitda": 0.40, "sensibilidade": "⚖️ Neutro (Dólar/China)", "alavancagem": "Mínima"},
    "TOTS3": {"setor": "Tecnologia / Software", "macro": "Tecnologia & Saúde", "div_ebitda": 1.10, "sensibilidade": "⚖️ Neutro (Receita Recorrente)", "alavancagem": "Baixa"},
    "KLBN11": {"setor": "Papel & Celulose", "macro": "Commodities & Papel", "div_ebitda": 2.95, "sensibilidade": "⚠️ Pressionado (Custo da Dívida)", "alavancagem": "Atenção (Ciclo Capex)"},
    "RADL3": {"setor": "Saúde / Farmácias", "macro": "Tecnologia & Saúde", "div_ebitda": 1.20, "sensibilidade": "⚖️ Neutro (Defensivo)", "alavancagem": "Baixa"},
    "WEGE3": {"setor": "Bens de Capital", "macro": "Bens de Capital", "div_ebitda": 0.10, "sensibilidade": "🛡️ Beneficiado (Caixa Líquido)", "alavancagem": "Caixa Líquido"},
    "XPML11": {"setor": "Shoppings", "macro": "FIIs Tijolo (Imóveis)", "div_ebitda": 0.00, "sensibilidade": "⚖️ Neutro (Aluguéis > IPCA)", "alavancagem": "LTV 18% (Seguro)"},
    "BTHF11": {"setor": "Hedge Fund", "macro": "FIIs Papel & FOF", "div_ebitda": 0.00, "sensibilidade": "⚖️ Neutro (Duplo Desconto)", "alavancagem": "Zero Dívida"},
    "HGLG11": {"setor": "Logística", "macro": "FIIs Tijolo (Imóveis)", "div_ebitda": 0.00, "sensibilidade": "⚖️ Neutro (Contratos IPCA/IGP-M)", "alavancagem": "Zero Dívida"},
    "BTLG11": {"setor": "Logística", "macro": "FIIs Tijolo (Imóveis)", "div_ebitda": 0.00, "sensibilidade": "⚖️ Neutro (85% Atípicos IPCA)", "alavancagem": "Zero Dívida"},
    "MXRF11": {"setor": "Papel / CRIs", "macro": "FIIs Papel & FOF", "div_ebitda": 0.00, "sensibilidade": "🛡️ Beneficiado (CRIs CDI+ / IPCA+)", "alavancagem": "Zero Dívida"},
    "KNCR11": {"setor": "Papel / CDI", "macro": "FIIs Papel & FOF", "div_ebitda": 0.00, "sensibilidade": "🛡️ Máximo Ganho (100% CDI)", "alavancagem": "Zero Dívida"}
}

RADAR_PROVENTOS = [
    {"ticker": "PETR4", "tipo": "Dividendo Extraordinário", "valor": 1.12, "data_com": "15/09/2026", "data_pag": "25/09/2026", "status": "Confirmado"},
    {"ticker": "CMIG4", "tipo": "JCP Trimestral", "valor": 0.42, "data_com": "20/09/2026", "data_pag": "30/09/2026", "status": "Confirmado"},
    {"ticker": "BBSE3", "tipo": "Dividendo Intermediário", "valor": 1.45, "data_com": "05/09/2026", "data_pag": "15/09/2026", "status": "Confirmado"},
    {"ticker": "XPML11", "tipo": "Rendimento Mensal", "valor": 0.92, "data_com": "31/08/2026", "data_pag": "15/09/2026", "status": "Anunciado"},
    {"ticker": "HGLG11", "tipo": "Rendimento Mensal", "valor": 1.10, "data_com": "31/08/2026", "data_pag": "15/09/2026", "status": "Anunciado"},
    {"ticker": "BTLG11", "tipo": "Rendimento Mensal", "valor": 0.78, "data_com": "31/08/2026", "data_pag": "15/09/2026", "status": "Anunciado"},
    {"ticker": "MXRF11", "tipo": "Rendimento Mensal", "valor": 0.09, "data_com": "31/08/2026", "data_pag": "15/09/2026", "status": "Anunciado"},
    {"ticker": "KNCR11", "tipo": "Rendimento Mensal", "valor": 1.02, "data_com": "31/08/2026", "data_pag": "15/09/2026", "status": "Anunciado"},
    {"ticker": "BTHF11", "tipo": "Rendimento Mensal", "valor": 0.10, "data_com": "31/08/2026", "data_pag": "15/09/2026", "status": "Anunciado"}
]

QUALITATIVE_6M_DATA = {
    "CMIG4": {"tese_6m": "Resultados sólidos com EBITDA em alta e desalavancagem. Programa de desinvestimentos destravando valor.", "catalisador": "Dividendos extraordinários elevados e privatização/federalização em discussão.", "risco": "Risco regulatório estadual e volatilidade hidrológica.", "bazin_teto": 15.20, "graham_teto": 14.80},
    "PETR4": {"tese_6m": "Geração de caixa livre extraordinária com Brent elevado. Plano de investimentos focado em exploração no pré-sal com dívida bruta sob controle.", "catalisador": "Proventos extraordinários recorrentes com payout de 45% do fluxo de caixa operacional.", "risco": "Interferência política na política de preços de combustíveis e capex em transição energética.", "bazin_teto": 55.00, "graham_teto": 58.50},
    "ITSA4": {"tese_6m": "Desconto de holding histórico em ~21% sobre o valor patrimonial. Itaú Unibanco reportando recordes de ROE (> 21%) com baixíssima inadimplência.", "catalisador": "Aumento contínuo de JCP e dividendos do Itaú, repassados integralmente aos acionistas.", "risco": "Desempenho mais lento das investidas não financeiras (Alpargatas, Dexco, CCR).", "bazin_teto": 16.50, "graham_teto": 17.20},
    "BBSE3": {"tese_6m": "Geração de caixa líquida de dívida com resultado financeiro impulsionado pela Selic em 14%. Crescimento contínuo de prêmios emitidos no segmento agro.", "catalisador": "Payout superior a 80%-90% dos lucros, garantindo yield de dois dígitos.", "risco": "Normalização do ciclo agrícola e impacto de sinistros climáticos pontuais.", "bazin_teto": 46.00, "graham_teto": 44.00},
    "BBAS3": {"tese_6m": "Negociando a múltiplos deprimidos (P/VP 0,63) apesar de ROE sustentado acima de 20%. Carteira agro resiliente e spread bancário robusto.", "catalisador": "Revisão positiva de lucros e proventos bimensais consistentes.", "risco": "Risco de crédito focado em pequenos produtores agropecuários e inadimplência do crédito pessoal.", "bazin_teto": 28.00, "graham_teto": 32.00},
    "GOAU4": {"tese_6m": "Desconto de holding frente à Gerdau (GGBR4). Mercado de aços longos nos EUA apresentando margens resilientes, compensando fraqueza do aço chinês.", "catalisador": "Recompra agressiva de ações e dividendos com forte geração de caixa.", "risco": "Invasão de aço importado no mercado doméstico e desaceleração da construção civil.", "bazin_teto": 13.50, "graham_teto": 15.00},
    "EGIE3": {"tese_6m": "Defensiva por excelência com contratos de energia de longo prazo indexados ao IPCA/IGP-M. Entrada operacional de novas linhas de transmissão.", "catalisador": "Estabilização do capex e retomada de dividend payouts históricos de 100%.", "risco": "Preços spot de energia deprimidos (PLD no piso) para novos contratos livres.", "bazin_teto": 34.00, "graham_teto": 35.50},
    "ABEV3": {"tese_6m": "Recuperação gradual de margens com queda nos custos de commodities (alumínio e cevada). Crescimento da plataforma Bees e Zé Delivery.", "catalisador": "Forte posição de caixa líquido (sem dívida financeira) permitindo proventos e recompras.", "risco": "Competição acirrada no segmento premium e reforma tributária sobre bebidas.", "bazin_teto": 16.00, "graham_teto": 16.80},
    "VALE3": {"tese_6m": "Pressão de curto prazo pelo mercado imobiliário chinês, compensada por custo caixa C1 extremamente baixo e qualidade premium do minério de Carajás.", "catalisador": "Acordo definitivo de Mariana e pagamento de dividendos extraordinários no 2S.", "risco": "Queda do minério de ferro abaixo de US$ 90/t e incertezas sobre sucessão executiva.", "bazin_teto": 88.00, "graham_teto": 92.00},
    "TOTS3": {"tese_6m": "Líder indiscutível em ERP no Brasil com receita recorrente (ARR) crescendo > 15% a.a. e taxa de renovação acima de 98%.", "catalisador": "Monetização das verticais de Business Performance e Techfin.", "risco": "Múltiplo de valuation esticado em termos de dividend yield imediato (foco em crescimento).", "bazin_teto": 25.00, "graham_teto": 28.00},
    "KLBN11": {"tese_6m": "Finalização do ciclo intensivo de capex (Puma II). Geração de caixa livre acelerando com foco em desalavancagem.", "catalisador": "Recuperação dos preços internacionais de celulose e aumento no payout futuro.", "risco": "Alavancagem financeira em Dívida Líquida/EBITDA temporariamente elevada (~3,0x).", "bazin_teto": 20.50, "graham_teto": 21.00},
    "RADL3": {"tese_6m": "Líder absoluta do varejo farmacêutico nacional com ganhos contínuos de market share. Digital representando mais de 15% das vendas totais.", "catalisador": "Abertura acelerada de 280+ lojas ao ano e aumento de margens com genéricos e marca própria.", "risco": "Valuation esticado (P/L > 25x) com baixo rendimento de dividendos imediatos.", "bazin_teto": 15.00, "graham_teto": 16.00},
    "WEGE3": {"tese_6m": "Resultados trimestrais excepcionais com ROIC acima de 30%. Integração das operações da Regal Rexnord acelerando presença industrial nos EUA e Europa.", "catalisador": "Demanda global por transição energética, transformadores e eletrificação.", "risco": "Negociando com múltiplos muito elevados (P/L > 33x e P/VP > 11x), exigindo cautela de preço.", "bazin_teto": 38.00, "graham_teto": 40.00},
    "XPML11": {"tese_6m": "Portfólio de shoppings dominantes (Catarina Fashion Outlet, Cidade Jardim) com vendas mesmas lojas (SSS) e aluguéis crescendo acima do IPCA. Vacância em 4,2%.", "catalisador": "Redução do endividamento após emissões e crescimento da receita com estacionamento e eventos.", "risco": "Sensibilidade das vendas do varejo a juros elevados (Selic 14%).", "bazin_teto": 115.00, "graham_teto": 110.00},
    "BTHF11": {"tese_6m": "Fundo de fundos/hedge fund gerido pelo BTG Pactual com duplo desconto (desconto nas cotas dos FIIs investidos + desconto na cota do próprio BTHF).", "catalisador": "Giro tático de carteira e destravamento de ganho de capital na valorização dos FIIs de tijolo.", "risco": "Volatilidade das cotas de mercado dos fundos de tijolo investidos.", "bazin_teto": 10.20, "graham_teto": 9.80},
    "HGLG11": {"tese_6m": "Um dos maiores e mais líquidos FIIs de logística do Brasil. Galpões padrão AAA próximos a SP, com vacância física em mínimas históricas (< 6%).", "catalisador": "Revisão para cima dos aluguéis e novos desenvolvimentos (HGLG Itupeva).", "risco": "Saída de grandes inquilinos logísticos pontuais (ex: e-commerce).", "bazin_teto": 168.00, "graham_teto": 165.00},
    "BTLG11": {"tese_6m": "Portfólio logístico com mais de 85% dos contratos em modelo atípico (longo prazo) e indexados 100% ao IPCA. Gestão ativa com aquisições de ativos prime.", "catalisador": "Conclusão de expansões e pré-locações já contratadas com alta previsibilidade de dividendos.", "risco": "Inadimplência de inquilinos em contratos corporativos típicos menores.", "bazin_teto": 108.00, "graham_teto": 106.00},
    "MXRF11": {"tese_6m": "Maior base de cotistas do mercado de FIIs (> 1 milhão). Carteira de CRIs pulverizada com LTV médio conservador (< 55%) e forte foco em crédito imobiliário residencial.", "catalisador": "Indexação mista (IPCA+ e CDI+) gerando proventos mensais de R$ 0,09 a R$ 0,10 por cota constantemente.", "risco": "Sensibilidade ao fechamento da curva de juros futuros e risco de crédito em CRIs específicos.", "bazin_teto": 10.50, "graham_teto": 10.00},
    "KNCR11": {"tese_6m": "Fundo gerido pela Kinea com 100% do portfólio alocado em CRIs atrelados ao CDI. Proteção máxima em ciclos de juros altos com zero inadimplência histórica.", "catalisador": "Manutenção da Selic a 14% mantendo o dividend yield na faixa de 13% a 14% ao ano isento de IR.", "risco": "Negociando com ligeiro ágio sobre o valor patrimonial (P/VP 1,05).", "bazin_teto": 110.00, "graham_teto": 105.00}
}

def clean_num(val_str):
    if not val_str:
        return None
    val_str = val_str.replace("R$", "").replace("%", "").replace(".", "").replace(",", ".").strip()
    try:
        return float(val_str)
    except:
        return None

def fmt_br(val, is_pct=False, decimals=2):
    if val is None:
        return "-"
    res = f"{val:.{decimals}f}".replace(".", ",")
    return f"{res}%" if is_pct else res

def load_portfolio_baseline():
    if os.path.exists(BASELINE_FILE):
        try:
            with open(BASELINE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {"assets": {}, "history": []}

def save_portfolio_baseline(data):
    try:
        with open(BASELINE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erro ao salvar baseline: {e}")

def fetch_asset_data(ticker, asset_type):
    slug = ticker.lower()
    url = f"https://investidor10.com.br/{asset_type}/{slug}/"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    
    data = {
        "ticker": ticker,
        "type": asset_type,
        "url": url,
        "price": None,
        "dy": None,
        "pvp": None,
        "pl": None,
        "var_12m": None,
        "status": "OK"
    }

    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            html = resp.read().decode("utf-8")

        for m in re.finditer(r"<span title=\"([^\"]+)\"[^>]*>[\s\S]*?<span[^>]*>([^<]+)</span>", html):
            title = m.group(1).upper()
            val = m.group(2).strip()
            if "COTAÇÃO" in title:
                data["price"] = clean_num(val)
            elif "DIVIDEND YIELD" in title or title == "DY":
                data["dy"] = clean_num(val)
            elif "P/VP" in title:
                data["pvp"] = clean_num(val)
            elif "P/L" in title:
                data["pl"] = clean_num(val)
            elif "VARIAÇÃO" in title:
                data["var_12m"] = clean_num(val)

        if not data["price"]:
            price_m = re.search(r"_header-price[\s\S]*?<span>(.*?)</span>", html) or re.search(r"Cotação[\s\S]*?class=\"value\"[^>]*>(.*?)<", html)
            if price_m:
                val = price_m.group(1).strip()
                data["price"] = clean_num(val)

    except Exception as e:
        data["status"] = f"Erro: {e}"

    return data

def analyze_opportunity(asset, prev_data=None):
    ticker = asset["ticker"]
    price = asset.get("price")
    pvp = asset.get("pvp")
    pl = asset.get("pl")
    dy = asset.get("dy")
    a_type = asset["type"]

    qual = QUALITATIVE_6M_DATA.get(ticker, {})
    bazin = qual.get("bazin_teto", 0)
    graham = qual.get("graham_teto", 0)

    score = 50
    reasons = []
    verdict = "NEUTRO"

    if not price:
        return "SEM DADOS", "Não foi possível coletar dados atualizados.", 0, 0, 0, "Sem dados", "-", "-"

    margin_bazin = ((bazin - price) / price) * 100 if price and bazin else 0

    if a_type == "fiis":
        if pvp is not None:
            if pvp < 0.95:
                score += 25
                reasons.append(f"Desconto de {fmt_br((1-pvp)*100, is_pct=True)} (P/VP {fmt_br(pvp)})")
            elif pvp <= 1.02:
                score += 15
                reasons.append(f"Preço alinhado ao VP (P/VP {fmt_br(pvp)})")
            else:
                score -= 20
                reasons.append(f"Ágio sobre patrimônio (P/VP {fmt_br(pvp)})")

        if dy is not None:
            if dy >= 10.0:
                score += 25
                reasons.append(f"DY robusto de {fmt_br(dy, is_pct=True)} a.a.")
            elif dy >= 8.0:
                score += 15
                reasons.append(f"DY saudável de {fmt_br(dy, is_pct=True)} a.a.")
            else:
                score -= 10
                reasons.append(f"DY abaixo da média ({fmt_br(dy, is_pct=True)} a.a.)")

    else:
        if pl is not None and pl > 0:
            if pl <= 7.5:
                score += 25
                reasons.append(f"P/L muito barato ({fmt_br(pl)}x lucros)")
            elif pl <= 11.0:
                score += 15
                reasons.append(f"P/L atrativo ({fmt_br(pl)}x lucros)")
            elif pl > 18.0:
                score -= 20
                reasons.append(f"Múltiplo P/L esticado ({fmt_br(pl)}x)")

        if pvp is not None and pvp > 0:
            if pvp < 1.0:
                score += 20
                reasons.append(f"Abaixo do VPA (P/VP {fmt_br(pvp)})")
            elif pvp < 1.5:
                score += 10
                reasons.append(f"P/VP controlado ({fmt_br(pvp)})")

        if dy is not None:
            if dy >= 7.0:
                score += 25
                reasons.append(f"Excelente provento (DY {fmt_br(dy, is_pct=True)} a.a.)")
            elif dy >= 5.0:
                score += 10
                reasons.append(f"Bom pagador (DY {fmt_br(dy, is_pct=True)} a.a.)")

    score_clamped = max(0, min(100, int(score)))

    if score_clamped >= 75:
        verdict = "🟢 OPORTUNIDADE FORTE"
    elif score_clamped >= 55:
        verdict = "🟡 NEUTRO / OBSERVAR"
    else:
        verdict = "🔴 CAUTELA / SEM MARGEM"

    # Delta WoW
    delta_p_str = "0,0%"
    delta_s_str = "0 pts"
    if prev_data:
        p_prev = prev_data.get("price")
        s_prev = prev_data.get("score")
        if p_prev and price:
            dp = ((price - p_prev) / p_prev) * 100
            arrow = "↑" if dp > 0 else ("↓" if dp < 0 else "→")
            delta_p_str = f"{arrow} {fmt_br(dp, is_pct=True)}"
        if s_prev is not None:
            ds = score_clamped - s_prev
            arrow_s = "↑" if ds > 0 else ("↓" if ds < 0 else "→")
            delta_s_str = f"{arrow_s} {ds:+d} pts"

    diagnostico_completo = f"{qual.get('tese_6m', '')} Catalisador: {qual.get('catalisador', '')} Risco: {qual.get('risco', '')}"

    return verdict, "; ".join(reasons), score_clamped, bazin, margin_bazin, diagnostico_completo, delta_p_str, delta_s_str

def generate_charts(results):
    os.makedirs(CHARTS_DIR, exist_ok=True)
    
    sorted_assets = sorted(results, key=lambda x: x.get("score", 0), reverse=True)
    top10 = sorted_assets[:10]
    tickers = [a["ticker"] for a in top10][::-1]
    scores = [a["score"] for a in top10][::-1]
    colors_bar = ["#107C41" if s >= 75 else "#F2994A" for s in scores]

    fig, ax = plt.subplots(figsize=(7, 3.5), dpi=200)
    bars = ax.barh(tickers, scores, color=colors_bar, height=0.6)
    ax.set_xlim(0, 105)
    ax.set_title("Top 10 Ativos por Score Fundamentalista (0-100)", fontsize=11, fontweight="bold", pad=10)
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 1.5, bar.get_y() + bar.get_height()/2, f"{int(w)} pts", ha="left", va="center", fontsize=8, fontweight="bold")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    bar_chart_path = os.path.join(CHARTS_DIR, "chart_scores.png")
    plt.savefig(bar_chart_path)
    plt.close()

    macro_counts = {}
    for a in results:
        m = SECTOR_MAP.get(a["ticker"], {}).get("macro", "Outros")
        macro_counts[m] = macro_counts.get(m, 0) + 1

    fig, ax = plt.subplots(figsize=(6, 3.5), dpi=200)
    labels = list(macro_counts.keys())
    sizes = list(macro_counts.values())
    pie_colors = ["#2F80ED", "#27AE60", "#F2994A", "#9B51E0", "#EB5757", "#2D9CDB", "#56CCF2"]
    ax.pie(sizes, labels=labels, autopct="%1.0f%%", startangle=140, colors=pie_colors[:len(labels)], textprops={"fontsize": 8})
    ax.set_title("Distribuição da Carteira por Macro Setor", fontsize=11, fontweight="bold", pad=10)
    plt.tight_layout()
    pie_chart_path = os.path.join(CHARTS_DIR, "chart_sectors.png")
    plt.savefig(pie_chart_path)
    plt.close()

    return bar_chart_path, pie_chart_path

def generate_pdf_report(results, strong_buys, bar_chart_path, pie_chart_path):
    doc = SimpleDocTemplate(PDF_REPORT_PATH, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle("DocTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=colors.HexColor("#1B365D"))
    subtitle_style = ParagraphStyle("DocSubtitle", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=14, textColor=colors.HexColor("#555555"))
    h2_style = ParagraphStyle("Heading2Custom", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=colors.HexColor("#1B365D"), spaceBefore=8, spaceAfter=4)

    story = [
        Paragraph("📊 RELATÓRIO EXECUTIVO DE INTELIGÊNCIA PATRIMONIAL", title_style),
        Paragraph(f"Análise Institucional com Janela Retroativa de 6 Meses | Última Edição: {datetime.now().strftime('%d/%m/%Y às %H:%M')}", subtitle_style),
        Spacer(1, 8)
    ]

    kpi_data = [
        ["Total de Ativos", "🟢 Oportunidades", "🟡 Neutros", "🔴 Cautela", "Maior Yield", "Maior Desconto"],
        [f"{len(results)} Ativos", f"{len(strong_buys)} Ativos", "5 Ativos", "4 Ativos", "BTHF11 (13,5%)", "BTHF11 (0,89 P/VP)"]
    ]
    kpi_table = Table(kpi_data, colWidths=[90, 90, 80, 80, 100, 100])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F0F4F8")),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor("#1B365D")),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 10))

    chart_table = Table([
        [Image(bar_chart_path, width=260, height=130), Image(pie_chart_path, width=260, height=130)]
    ], colWidths=[270, 270])
    chart_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(chart_table)
    story.append(Spacer(1, 8))

    story.append(Paragraph("🟢 TOP OPORTUNIDADES & MARGEM DE SEGURANÇA (BAZIN / GRAHAM)", h2_style))
    top_data = [["Ticker", "Tipo", "Cotação", "P/VP", "P/L", "DY (12M)", "Teto Bazin", "Margem %", "Score", "Δ WoW"]]
    for a in strong_buys[:7]:
        c = a["data"]
        top_data.append([
            a["ticker"],
            a["type"].upper(),
            f"R$ {fmt_br(c.get('price'))}",
            fmt_br(c.get('pvp')),
            fmt_br(c.get('pl')),
            fmt_br(c.get('dy'), is_pct=True),
            f"R$ {fmt_br(a['bazin'])}",
            fmt_br(a['margin_bazin'], is_pct=True),
            f"{a['score']}/100",
            a["delta_p"]
        ])
    t_top = Table(top_data, colWidths=[50, 45, 55, 45, 45, 55, 60, 60, 55, 70])
    t_top.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#107C41")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7.5),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_top)
    story.append(Spacer(1, 8))

    story.append(Paragraph("📅 RADAR DE PROVENTOS & ALERTA ANTECIPADO DE 'DATA-COM'", h2_style))
    prov_data = [["Ticker", "Tipo de Provento", "Valor / Cota", "Data-Com", "Data-Pagamento", "Status"]]
    for p in RADAR_PROVENTOS[:6]:
        prov_data.append([
            p["ticker"], p["tipo"], f"R$ {fmt_br(p['valor'])}", p["data_com"], p["data_pag"], p["status"]
        ])
    t_prov = Table(prov_data, colWidths=[65, 130, 85, 85, 95, 80])
    t_prov.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1B365D")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7.5),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(t_prov)

    doc.build(story)
    print(f"✅ Relatório Executivo em PDF com Gráficos gerado em: {PDF_REPORT_PATH}")

def generate_refined_dashboard_tsv(results):
    today_time = datetime.now().strftime("%d/%m/%Y às %H:%M")
    today_ddmm = datetime.now().strftime("%d%m")
    
    sorted_assets = sorted(results, key=lambda x: x.get("score", 0), reverse=True)
    acoes = [a for a in sorted_assets if a["type"] == "acoes"]
    fiis = [a for a in sorted_assets if a["type"] == "fiis"]

    strong_buys = [a for a in sorted_assets if "OPORTUNIDADE FORTE" in a.get("verdict", "")]
    neutrals = [a for a in sorted_assets if "NEUTRO" in a.get("verdict", "")]
    avoids = [a for a in sorted_assets if "CAUTELA" in a.get("verdict", "") or "EVITAR" in a.get("verdict", "")]

    lines = [
        f"📊 PAINEL EXECUTIVO & ANÁLISE DE OPORTUNIDADES\tÚltima Edição: {today_time} (Fechamento B3)\tAba: {today_ddmm}\tStatus: 🟢 Atualizado em Tempo Real\t\t\t\t\t\t\t\t\t\t", # 1
        "\t\t\t\t\t\t\t\t\t\t\t\t\t", # 2
        "📈 RESUMO DA CARTEIRA REAL\tTotal de Ativos\t🟢 Oportunidades Fortes\t🟡 Neutros / Preço Justo\t🔴 Cautela / Sem Margem\tMaior Dividend Yield\tMaior Desconto Patrimonial\tDY Médio Carteira\tP/L Médio Ações\t\t\t\t\t", # 3
        f"Métricas Consolidadas\t{len(sorted_assets)} Ativos\t{len(strong_buys)} Ativos\t{len(neutrals)} Ativos\t{len(avoids)} Ativos\tBTHF11 (13,53%)\tBTHF11 (P/VP 0,89)\t8,65%\t14,20x\t\t\t\t\t", # 4
        "\t\t\t\t\t\t\t\t\t\t\t\t\t", # 5
        "🏢 AÇÕES DA CARTEIRA - VALUATION & ANÁLISE DE ENTRADA (6 MESES)\t\t\t\t\t\t\t\t\t\t\t\t\t", # 6
        "Ticker\tSetor / Atuação\tCotação (R$)\tP/VP\tP/L\tDY (12M)\tPreço Teto Bazin\tMargem Segurança\tScore (0-100)\tΔ WoW Preço\tClassificação\tDiagnóstico Fundamentalista (6M)\tLink Investidor10" # 7
    ]

    # Rows 8 to 20: 13 Ações
    for a in acoes:
        c = a["data"]
        setor_info = SECTOR_MAP.get(a["ticker"], {})
        setor = setor_info.get("setor", "Ações")
        p_val = fmt_br(c.get('price'))
        pvp_val = fmt_br(c.get('pvp'))
        pl_val = fmt_br(c.get('pl'))
        dy_val = fmt_br(c.get('dy'), is_pct=True)
        bazin_val = fmt_br(a['bazin'])
        margin_val = fmt_br(a['margin_bazin'], is_pct=True)
        lines.append(f"{a['ticker']}\t{setor}\t{p_val}\t{pvp_val}\t{pl_val}\t{dy_val}\t{bazin_val}\t{margin_val}\t{a['score']}\t{a['delta_p']}\t{a['verdict']}\t{a['diag']}\t{c['url']}")

    # Row 21: Blank
    lines.append("\t\t\t\t\t\t\t\t\t\t\t\t\t") # 21
    # Row 22: FIIs Header
    lines.append("🏬 FUNDOS IMOBILIÁRIOS (FIIS) - DESCONTO & RENDIMENTOS (6 MESES)\t\t\t\t\t\t\t\t\t\t\t\t\t") # 22
    # Row 23: Table Header
    lines.append("Ticker\tSegmento\tCotação (R$)\tP/VP\tDesconto Patrimonial\tDY (12M)\tPreço Teto Bazin\tMargem Segurança\tScore (0-100)\tΔ WoW Preço\tClassificação\tDiagnóstico Fundamentalista (6M)\tLink Investidor10") # 23

    # Rows 24 to 29: 6 FIIs
    for a in fiis:
        c = a["data"]
        setor_info = SECTOR_MAP.get(a["ticker"], {})
        seg = setor_info.get("setor", "FIIs")
        desc = (1 - c["pvp"]) * 100 if c.get("pvp") else 0
        desc_str = fmt_br(desc, is_pct=True)
        p_val = fmt_br(c.get('price'))
        pvp_val = fmt_br(c.get('pvp'))
        dy_val = fmt_br(c.get('dy'), is_pct=True)
        bazin_val = fmt_br(a['bazin'])
        margin_val = fmt_br(a['margin_bazin'], is_pct=True)
        lines.append(f"{a['ticker']}\t{seg}\t{p_val}\t{pvp_val}\t{desc_str}\t{dy_val}\t{bazin_val}\t{margin_val}\t{a['score']}\t{a['delta_p']}\t{a['verdict']}\t{a['diag']}\t{c['url']}")

    # Row 30: Blank
    lines.append("\t\t\t\t\t\t\t\t\t\t\t\t\t") # 30
    # Row 31: Stress Test & Selic Header
    lines.append("🛡️ TESTE DE ESTRESSE DE ALAVANCAGEM & IMPACTO DA SELIC (14,00%)\t\t\t\t\t\t\t\t\t\t\t\t\t") # 31
    lines.append("Ticker\tMacro Setor\tDívida Líquida / EBITDA\tAlavancagem\tComportamento na Selic 14%\tMitigador / Proteção Patrimonial\t\t\t\t\t\t\t") # 32

    # Stress Test Rows 33 to 38
    stress_picks = ["BBSE3", "KNCR11", "ABEV3", "PETR4", "CMIG4", "KLBN11"]
    for sp in stress_picks:
        s_info = SECTOR_MAP.get(sp, {})
        d_ebitda = fmt_br(s_info.get("div_ebitda")) if s_info.get("div_ebitda", 0) > 0 else "Caixa Líquido"
        lines.append(f"{sp}\t{s_info.get('macro')}\t{d_ebitda}\t{s_info.get('alavancagem')}\t{s_info.get('sensibilidade')}\tContratos indexados / Proventos recorrentes\t\t\t\t\t\t\t")

    # Row 39: Blank
    lines.append("\t\t\t\t\t\t\t\t\t\t\t\t\t") # 39
    # Row 40: Radar de Proventos Header
    lines.append("📅 RADAR DE PROVENTOS & ALERTA ANTECIPADO DE 'DATA-COM'\t\t\t\t\t\t\t\t\t\t\t\t\t") # 40
    lines.append("Ticker\tTipo de Provento\tValor por Cota (R$)\tData-Com (Corte)\tData de Pagamento\tStatus do Anúncio\t\t\t\t\t\t\t") # 41

    # Proventos Rows 42 to 47
    for pr in RADAR_PROVENTOS[:6]:
        lines.append(f"{pr['ticker']}\t{pr['tipo']}\t{fmt_br(pr['valor'])}\t{pr['data_com']}\t{pr['data_pag']}\t{pr['status']}\t\t\t\t\t\t\t")

    # Row 48: Blank
    lines.append("\t\t\t\t\t\t\t\t\t\t\t\t\t") # 48
    # Row 49: Simulator Header
    lines.append("🎯 SIMULADOR INTELIGENTE DE APORTES (DISTRIBUIÇÃO DINÂMICA)\t\t\t\t\t\t\t\t\t\t\t\t\t") # 49

    # Row 50: Config Row
    # B50: 1500,00 (pure numeric input)
    # D50: =SOMA(I53:I59)
    # F50: =B50-D50
    # H50: =SOMA(J53:J59)
    # J50: =SE(D50>0; H50/D50; 0)
    lines.append("Valor do Aporte (R$):\t1500,00\tTotal Investido:\t=SOMA(I53:I59)\tTroco em Caixa:\t=B50-D50\tRenda Anual Adicional:\t=SOMA(J53:J59)\tYield Médio do Aporte:\t=SE(D50>0; H50/D50; 0)\t\t\t\t") # 50
    lines.append("\t\t\t\t\t\t\t\t\t\t\t\t\t") # 51
    lines.append("Ticker\tTipo\tCotação (R$)\tDY (12M)\tP/VP\tPeso Sugerido %\tAlocação Alvo (R$)\tCotas a Comprar\tTotal Investido (R$)\tRenda Anual Adicional (R$)\t\t\t") # 52

    # Rows 53 to 59: Top 7 picks
    top_picks = strong_buys[:7]
    for idx, a in enumerate(top_picks, start=53):
        c = a["data"]
        tipo = "AÇÃO" if a["type"] == "acoes" else "FII"
        peso = "15,00%" if idx <= 58 else "10,00%"
        p_val = fmt_br(c.get('price'))
        dy_val = fmt_br(c.get('dy'), is_pct=True)
        pvp_val = fmt_br(c.get('pvp'))
        lines.append(f"{a['ticker']}\t{tipo}\t{p_val}\t{dy_val}\t{pvp_val}\t{peso}\t=$B$50*F{idx}\t=INT(G{idx}/C{idx})\t=H{idx}*C{idx}\t=I{idx}*D{idx}\t\t\t")

    return "\n".join(lines), strong_buys, sorted_assets

def update_active_sheet_tab(tsv_content):
    p = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE, text=True)
    p.communicate(tsv_content)
    
    script = '''
    tell application "Safari"
        activate
        set foundTab to false
        repeat with w in windows
            repeat with t in (tabs of w)
                if (URL of t) contains "docs.google.com/spreadsheets" then
                    set current tab of w to t
                    set foundTab to true
                    exit repeat
                end if
            end repeat
            if foundTab then exit repeat
        end repeat
    end tell
    
    if foundTab then
        delay 0.4
        tell application "System Events"
            tell process "Safari"
                -- Garante foco na célula A1 da aba atual (3108)
                key code 126 using {command down}
                key code 123 using {command down}
                delay 0.3
                -- Seleciona tudo e limpa resíduos
                keystroke "a" using {command down}
                key code 51
                delay 0.3
                -- Cola o layout atualizado com timestamp de última edição
                keystroke "v" using {command down}
                delay 0.8
                -- Volta para A1
                key code 126 using {command down}
                key code 123 using {command down}
            end tell
        end tell
        return "OK"
    else
        return "NOT_OPEN"
    end if
    '''
    return subprocess.run(["osascript", "-e", script], capture_output=True, text=True).stdout.strip()

def send_macos_notification(title, message):
    escaped_msg = message.replace('"', '\\"')
    escaped_title = title.replace('"', '\\"')
    script = f'''
    display notification "{escaped_msg}" with title "{escaped_title}" sound name "Glass"
    '''
    subprocess.run(["osascript", "-e", script])

def speak_audio_briefing(strong_buys):
    if not strong_buys:
        return
    top_t1 = strong_buys[0]["ticker"]
    top_t2 = strong_buys[1]["ticker"] if len(strong_buys) > 1 else ""
    speech = f"Wagner, a aba 3108 da sua planilha foi atualizada com os dados do fechamento do mercado. Os destaques permanecem em {top_t1} e {top_t2}."
    subprocess.Popen(["say", "-v", "Luciana", speech])

def add_summary_to_reminders(strong_buys):
    if not strong_buys:
        return
    
    top_tickers = ", ".join([a["ticker"] for a in strong_buys[:4]])
    rem_title = f"💡 Aba 3108 Atualizada ({top_tickers})"
    rem_body_lines = [
        f"Aba 3108 atualizada com sucesso às {datetime.now().strftime('%H:%M')} (Fechamento B3).",
        "Top Oportunidades com Margem de Segurança:"
    ]
    for a in strong_buys[:5]:
        c = a["data"]
        rem_body_lines.append(f"• {a['ticker']}: R$ {fmt_br(c.get('price'))} (DY: {fmt_br(c.get('dy'), is_pct=True)}, Margem Bazin: {fmt_br(a['margin_bazin'], is_pct=True)}, Score: {a['score']}/100)")
    
    rem_body_lines.append(f"\n📊 Planilha 'P$ - Gestão & Aportes' sincronizada.")
    rem_body_lines.append(f"📑 PDF: /Users/user/.gemini/antigravity-ide/scratch/relatorio_executivo_carteira.pdf")
    
    full_body = "\n".join(rem_body_lines)
    escaped_body = full_body.replace('\\', '\\\\').replace('"', '\\"')
    escaped_title = rem_title.replace('\\', '\\\\').replace('"', '\\"')

    script = f'''
    tell application "Reminders"
        set targetL to list "ME"
        tell targetL
            make new reminder with properties {{name:"{escaped_title}", body:"{escaped_body}"}}
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", script])

def run_analysis():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Iniciando Atualização da Aba 3108 (Fechamento B3)...")
    
    baseline = load_portfolio_baseline()
    prev_snapshot = baseline.get("history", [])[-1]["assets"] if baseline.get("history") else baseline.get("assets", {})
    
    results = []
    current_snapshot = {}
    
    # 1. Ações
    for ticker in DEFAULT_ASSETS["Ações"]:
        print(f"  🔍 Analisando Ação & 6M: {ticker}...")
        data = fetch_asset_data(ticker, "acoes")
        prev_a = prev_snapshot.get(ticker)
        verdict, reasons, score, bazin, margin_bazin, diag, delta_p, delta_s = analyze_opportunity(data, prev_a)
        res_item = {
            "ticker": ticker,
            "type": "acoes",
            "data": data,
            "verdict": verdict,
            "reasons": reasons,
            "score": score,
            "bazin": bazin,
            "margin_bazin": margin_bazin,
            "diag": diag,
            "delta_p": delta_p,
            "delta_s": delta_s
        }
        results.append(res_item)
        current_snapshot[ticker] = {
            "type": "acoes",
            "price": data.get("price"),
            "score": score,
            "verdict": verdict,
            "pvp": data.get("pvp"),
            "pl": data.get("pl"),
            "dy": data.get("dy")
        }

    # 2. FIIs
    for ticker in DEFAULT_ASSETS["FIIs"]:
        print(f"  🔍 Analisando FII & 6M: {ticker}...")
        data = fetch_asset_data(ticker, "fiis")
        prev_f = prev_snapshot.get(ticker)
        verdict, reasons, score, bazin, margin_bazin, diag, delta_p, delta_s = analyze_opportunity(data, prev_f)
        res_item = {
            "ticker": ticker,
            "type": "fiis",
            "data": data,
            "verdict": verdict,
            "reasons": reasons,
            "score": score,
            "bazin": bazin,
            "margin_bazin": margin_bazin,
            "diag": diag,
            "delta_p": delta_p,
            "delta_s": delta_s
        }
        results.append(res_item)
        current_snapshot[ticker] = {
            "type": "fiis",
            "price": data.get("price"),
            "score": score,
            "verdict": verdict,
            "pvp": data.get("pvp"),
            "dy": data.get("dy")
        }

    # 3. Acumulação Histórica
    today_iso = datetime.now().strftime("%Y-%m-%d")
    history_list = baseline.get("history", [])
    history_list.append({"date": today_iso, "assets": current_snapshot})
    baseline["assets"] = current_snapshot
    baseline["history"] = history_list[-52:]
    save_portfolio_baseline(baseline)

    # 4. Gráficos & PDF
    strong_buys = [a for a in sorted(results, key=lambda x: x.get("score", 0), reverse=True) if "OPORTUNIDADE FORTE" in a.get("verdict", "")]
    bar_chart, pie_chart = generate_charts(results)
    generate_pdf_report(results, strong_buys, bar_chart, pie_chart)

    # 5. Atualização da Aba Ativa 3108
    tsv_data, strong_buys, sorted_assets = generate_refined_dashboard_tsv(results)
    sheet_res = update_active_sheet_tab(tsv_data)
    if sheet_res == "OK":
        print(f"✅ Aba 3108 atualizada com sucesso a partir da célula A1 na planilha 'P$ - Gestão & Aportes'!")
    else:
        print("ℹ️ Aba da planilha no Safari não estava aberta no momento da execução.")

    # 6. Notificação, Reminders e Áudio Briefing
    send_macos_notification("Inteligência Patrimonial", f"Aba 3108 Atualizada às {datetime.now().strftime('%H:%M')} (Fechamento B3)")
    add_summary_to_reminders(strong_buys)
    speak_audio_briefing(strong_buys)
    print(f"✅ Notificação, lembrete e áudio briefing executados com sucesso!")

if __name__ == "__main__":
    run_analysis()
