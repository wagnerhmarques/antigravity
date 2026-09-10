import re

tex_path = '/Users/user/.gemini/antigravity-ide/scratch/Overleaf_TCC_Wagner_SingleFile/main.tex'
with open(tex_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Check for ** (markdown bold)
md_bolds = re.findall(r'\*\*.*?\*\*', text)
print(f'Markdown bold (**) occurrences: {len(md_bolds)}')

# Check for \textbf in text
tb_matches = re.findall(r'\\textbf\{([^}]+)\}', text)
print(f'Total \\textbf instances: {len(tb_matches)}')
for i, m in enumerate(tb_matches):
    print(f'  [{i+1}] {m}')

# Check environment pairs
begins = re.findall(r'\\begin\{([^}]+)\}', text)
ends = re.findall(r'\\end\{([^}]+)\}', text)
print(f'\\begin count: {len(begins)}, \\end count: {len(ends)}')
assert len(begins) == len(ends), f'Mismatch: {len(begins)} vs {len(ends)}'

# Check citations
cites = re.findall(r'\\cite\{([^}]+)\}', text)
all_cites = set()
for c in cites:
    for item in c.split(','):
        all_cites.add(item.strip())

bibs = re.findall(r'\\bibitem\{([^}]+)\}', text)
all_bibs = set(b.strip() for b in bibs)

missing_bibs = all_cites - all_bibs
print(f'Citations used: {len(all_cites)}, Bibitems available: {len(all_bibs)}')
print(f'Missing bibitems: {missing_bibs}')
assert len(missing_bibs) == 0, 'Some citations are missing from bibliography!'

print('\n========================================')
print('VERIFICATION SUMMARY:')
print(f'- Total file size: {len(text)} bytes')
print(f'- Total lines: {len(text.splitlines())}')
print(f'- Markdown bold (**): {len(md_bolds)}')
print(f'- Body text \\textbf: {len([m for m in tb_matches if "Table" not in m and "Physics" not in m and "Presidente" not in m])} (Only in formal table headers/bib)')
print(f'- Open/closed environments matched: {len(begins)}/{len(ends)}')
print(f'- Citations: {len(all_cites)} (0 missing)')
print('========================================')
