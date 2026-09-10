import os
import re

fig_dir = '/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile/figuras'
tex_file = '/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile/main.tex'

with open(tex_file) as f:
    text = f.read()

# Check all incluirfigura and includegraphics
incs = re.findall(r'\\(?:incluirfigura|includegraphics)(?:\[[^\]]*\])?\{([^}]+)\}', text)
print("=== VERIFICAÇÃO DE FIGURAS NO LATEX ===")
for inc in incs:
    p = os.path.join(fig_dir, inc)
    exists = os.path.exists(p)
    size = os.path.getsize(p) if exists else 0
    print(f"Arquivo: {inc:<38} | Existe: {str(exists):<5} | Tamanho: {size} bytes")

# Check markdown bold
bold_matches = re.findall(r'\*\*[^*]+\*\*', text)
print(f"\nMarkdown bold count: {len(bold_matches)}")

# Check hyperref math shift
href_math = re.findall(r'\\(?:section|subsection|subsubsection|chapter|caption)\{[^}]*\$[^}]*\}', text)
print(f"Math in headers/captions (short captions used?): {len(href_math)}")

# Check begin/end balance
begins = re.findall(r'\\begin\{([^}]+)\}', text)
ends = re.findall(r'\\end\{([^}]+)\}', text)
print(f"Total \\begin: {len(begins)} | Total \\end: {len(ends)} | Balance: {len(begins) == len(ends)}")
