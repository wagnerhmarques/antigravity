from pathlib import Path
import re

VAULT_DIR = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me")

def check_file(f):
    txt = f.read_text(encoding="utf-8")
    rel = f.relative_to(VAULT_DIR)
    
    math_segments = []
    for m in re.finditer(r'\$\$(.*?)\$\$', txt, re.DOTALL):
        math_segments.append(('block', m.group(1), m.start()))
    for m in re.finditer(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', txt):
        math_segments.append(('inline', m.group(1), m.start()))
        
    issues = []
    for kind, math_code, pos in math_segments:
        # 1. Unbalanced braces
        open_b = math_code.count('{')
        close_b = math_code.count('}')
        if open_b != close_b:
            issues.append(f'Chaves desbalanceadas ({open_b} vs {close_b}): {repr(math_code.strip()[:80])}')
            
        # 2. Delimitadores \left e \right descasados
        left_count = len(re.findall(r'\\left\b', math_code))
        right_count = len(re.findall(r'\\right\b', math_code))
        if left_count != right_count:
            issues.append(f'Delimitadores descasados ({left_count} \\left vs {right_count} \\right): {repr(math_code.strip()[:80])}')
            
        # 3. Comandos sem barra invertida
        suspicious = ['Delta', 'sigma', 'theta', 'alpha', 'beta', 'gamma', 'mu', 'int', 'iint', 'sum', 'prod', 'sqrt', 'cdot', 'times', 'pi', 'infty', 'frac']
        for word in suspicious:
            for match in re.finditer(r'(?<![\\a-zA-Z])' + word + r'\b', math_code):
                prefix = math_code[:match.start()]
                if 'text{' in prefix and prefix.count('{') > prefix.count('}'):
                    continue
                issues.append(f'Comando sem barra invertida ("{word}") em: {repr(math_code.strip()[:80])}')
                break

    if re.search(r'\$\$\s*\$\$', txt):
        issues.append('Bloco $$ vazio encontrado no arquivo')

    if issues:
        print(f"\n=== {rel} ({len(issues)} inconsistências) ===")
        for iss in issues:
            print(f"  ❌ {iss}")

if __name__ == "__main__":
    for f in sorted(VAULT_DIR.rglob("*.md")):
        check_file(f)
