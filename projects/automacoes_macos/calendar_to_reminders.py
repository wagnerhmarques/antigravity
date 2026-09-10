#!/usr/bin/env python3
"""
Sync Calendar Events to Reminders with Strategic Lists & Native Section Assignment.
Horizonte Mensal: Últimos 7 dias até os Próximos 35 dias (+1 mês).

Strategic Lists:
- TUTORMUNDI (TutorMundi calendar, meetings, school deals)
- USP (USP calendar, ICESP, TCC, academic research) -> [CRP, Graduação, CoC, Doutorado]
- SOFTSET (Softset, Lead resumption, Operations) -> [Ferramenta de IA..., Quadro de dosímetros]
- ME (Personal & Family)

100% Free, Native macOS automation.
"""

import subprocess
import json
import re
import sys
import time
from datetime import datetime

CALENDAR_TARGETS = [
    ("wagner.marques@tutormundi.com", "TUTORMUNDI"),
    ("wagner.marques@usp.br", "USP"),
    ("wagner.fmusp@gmail.com", "USP"),
    ("DNA-AgNCs - ICESP", "USP"),
    ("Trabalho", "SOFTSET"),
    ("Retomadas de LEAD ", "SOFTSET"),
    ("Wagner H Marques", "ME"),
    ("Pessoal", "ME"),
    ("Família", "ME")
]

def run_applescript(script):
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip(), res.stderr.strip()

def get_target_list(cal_name, event_title, event_notes):
    full_text = f"{cal_name} {event_title} {event_notes}".lower()
    if "tutormundi" in cal_name.lower() or "tutormundi" in full_text:
        return "TUTORMUNDI"
    if any(k in cal_name.lower() for k in ["usp.br", "fmusp", "icesp"]) or any(k in full_text for k in ["usp", "icesp", "fmusp", "tcc", "inrad", "física usp"]):
        return "USP"
    if any(k in cal_name.lower() for k in ["trabalho", "lead"]) or "softset" in full_text:
        return "SOFTSET"
    return "ME"

def extract_links_and_docs(text):
    links = re.findall(r'https?://[^\s<>"\'\)]+', text)
    filtered_links = []
    for l in links:
        if any(k in l.lower() for k in ["docs.google", "drive.google", "meet.google", "granola", "otter.ai", "fireflies", "tactiq", "notion", "activehosted", "zoom.us", "teams", "deal", "transcript", "even3"]):
            filtered_links.append(l)
        elif len(links) <= 2:
            filtered_links.append(l)
    return list(dict.fromkeys(filtered_links))

def ensure_reminders_lists_exist():
    required = ["TUTORMUNDI", "USP", "SOFTSET", "ME"]
    req_json = json.dumps(required)
    script = f'''
    tell application "Reminders"
        set existing to name of every list
        repeat with l in {req_json}
            if l is not in existing then
                make new list with properties {{name:l}}
            end if
        end repeat
    end tell
    '''
    run_applescript(script)

def organize_usp_sections_ui():
    script = '''
    tell application "Reminders"
        activate
        show list "USP"
    end tell
    delay 0.5
    tell application "System Events"
        tell process "Reminders"
            set layoutArea to UI element 1 of (UI elements of splitter group 1 of window 1 whose role is "AXLayoutArea")
            set outl to outline 1 of scroll area 1 of layoutArea
            
            set rowCount to count of rows of outl
            repeat with i from rowCount to 1 by -1
                try
                    set r to row i of outl
                    set rDesc to ""
                    repeat with c in (UI elements of r)
                        set rDesc to rDesc & " " & (description of c as text)
                    end repeat
                    
                    if rDesc contains "Follow-up:" then
                        set targetSec to "Doutorado"
                        if rDesc contains "COC" or rDesc contains "FISMED" then
                            set targetSec to "CoC"
                        else if rDesc contains "TCC" or rDesc contains "GRADUA" then
                            set targetSec to "Graduação"
                        else if rDesc contains "CRP" then
                            set targetSec to "CRP"
                        end if
                        
                        click r
                        delay 0.15
                        set mFile to menu "File" of menu bar item "File" of menu bar 1
                        repeat with mi in (every menu item of mFile)
                            if name of mi starts with "Move to Section" then
                                try
                                    click menu item targetSec of menu 1 of mi
                                end try
                                exit repeat
                            end if
                        end repeat
                        delay 0.15
                    end if
                end try
            end repeat
        end tell
    end tell
    '''
    run_applescript(script)

def sync_events():
    ensure_reminders_lists_exist()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sincronizando com Horizonte Mensal (-7 dias / +35 dias)...")

    created_count = 0
    skipped_count = 0
    items_created = []

    # Janela mensal: últimos 7 dias até próximos 35 dias (+1 mês)
    for cal_name, default_list in CALENDAR_TARGETS:
        escaped_cal = cal_name.replace('"', '\\"')
        script = f'''
        tell application "Calendar"
            set outList to {{}}
            try
                set cal to calendar "{escaped_cal}"
                set startDate to (current date) - (7 * days)
                set endDate to (current date) + (35 * days)
                set evs to (every event of cal whose start date is greater than or equal to startDate and start date is less than or equal to endDate)
                repeat with ev in evs
                    set evTitle to summary of ev
                    set evStart to (start date of ev as string)
                    set evEnd to (end date of ev as string)
                    set evDesc to description of ev
                    set evUrl to url of ev
                    if evDesc is missing value then set evDesc to ""
                    if evUrl is missing value then set evUrl to ""
                    set end of outList to (evTitle & "|||" & evStart & "|||" & evEnd & "|||" & evUrl & "|||" & evDesc)
                end repeat
            end try
            set AppleScript's text item delimiters to "\\n---EVENT_DELIMITER---\\n"
            return outList as text
        end tell
        '''
        
        stdout, _ = run_applescript(script)
        if not stdout:
            continue

        raw_events = stdout.split("\n---EVENT_DELIMITER---\n")
        for raw in raw_events:
            parts = raw.split("|||")
            if len(parts) < 5:
                continue
            title, start_str, end_str, url, desc = parts[0], parts[1], parts[2], parts[3], parts[4]
            
            if any(w in title.lower() for w in ["férias", "day-off", "aniversário", "ocupado"]):
                continue

            target_list = get_target_list(cal_name, title, desc)
            follow_up_title = f"Follow-up: {title}"
            
            all_text = f"{url}\n{desc}"
            doc_links = extract_links_and_docs(all_text)
            
            body_parts = [
                f"📅 Reunião: {title}",
                f"⏰ Horário: {start_str}",
                f"📁 Eixo Estratégico: {target_list}",
                f"🗓 Calendário: {cal_name}"
            ]
            
            if doc_links:
                body_parts.append("\n📄 Documentos & Transcrições Detectados:")
                for lk in doc_links:
                    body_parts.append(f"  • {lk}")
                    
            clean_desc = re.sub(r'<[^>]+>', '', desc).strip()
            if clean_desc:
                body_parts.append(f"\n📝 Pauta / Notas da Reunião:\n{clean_desc[:600]}")
                
            final_body = "\n".join(body_parts)
            escaped_body = final_body.replace('\\', '\\\\').replace('"', '\\"')
            escaped_title = follow_up_title.replace('\\', '\\\\').replace('"', '\\"')

            check_script = f'''
            tell application "Reminders"
                set foundCount to 0
                repeat with lName in {{"TUTORMUNDI", "USP", "SOFTSET", "ME"}}
                    try
                        set targetL to list (lName as string)
                        set matchRems to (every reminder of targetL whose name is "{escaped_title}")
                        set foundCount to foundCount + (count of matchRems)
                    end try
                end repeat
                return foundCount
            end tell
            '''
            check_out, _ = run_applescript(check_script)
            if check_out and check_out != "0":
                skipped_count += 1
                continue

            create_script = f'''
            tell application "Reminders"
                set targetL to list "{target_list}"
                tell targetL
                    make new reminder with properties {{name:"{escaped_title}", body:"{escaped_body}"}}
                end tell
            end tell
            '''
            c_out, c_err = run_applescript(create_script)
            if not c_err:
                created_count += 1
                items_created.append((target_list, follow_up_title, len(doc_links)))

    if created_count > 0:
        organize_usp_sections_ui()

    print(f"\n✅ Sincronização Mensal concluída com sucesso!")
    print(f"   • Novos lembretes criados no horizonte mensal: {created_count}")
    print(f"   • Lembretes já existentes preservados: {skipped_count}\n")
    for l_name, t, docs_n in items_created:
        docs_badge = f" [📎 {docs_n} link(s) de transcrição/doc]" if docs_n else ""
        print(f"   ➔ [{l_name}] {t}{docs_badge}")

if __name__ == "__main__":
    sync_events()
