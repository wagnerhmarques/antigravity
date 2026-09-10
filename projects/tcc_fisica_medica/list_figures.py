import re

with open('/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile/main.tex') as f:
    text = f.read()

chapters = text.split(r'\chapter{')
for ch_idx, ch_text in enumerate(chapters[1:], 1):
    ch_title = ch_text.split('}')[0]
    figs = ch_text.split(r'\begin{figure}')
    for fig_idx, fcontent in enumerate(figs[1:], 1):
        fpart = fcontent.split(r'\end{figure}')[0]
        cap_m = re.search(r'\\caption\s*\{([^}]+)\}', fpart, re.DOTALL)
        lab_m = re.search(r'\\label\s*\{([^}]+)\}', fpart)
        inc_m = re.search(r'\\includegraphics(?:\s*\[[^\]]*\])?\s*\{([^}]+)\}', fpart)
        tikz = 'tikzpicture' in fpart
        
        cap = cap_m.group(1).replace('\n', ' ').strip() if cap_m else "NO CAPTION"
        lab = lab_m.group(1).strip() if lab_m else "NO LABEL"
        inc = inc_m.group(1).strip() if inc_m else ("TikZ Native" if tikz else "NO GRAPHIC")
        print(f"Figura {ch_idx}.{fig_idx} (Label: {lab}) -> File: {inc}")
        print(f"   Caption: {cap[:90]}")
