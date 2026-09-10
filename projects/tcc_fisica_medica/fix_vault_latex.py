#!/usr/bin/env python3
"""
Corretor e Sanitizador de LaTeX para todas as notas do Vault
Substitui caracteres de controle corrompidos (form feed, tabs em comandos, carriage returns)
por comandos LaTeX válidos (\frac, \text, \theta, \right, \Delta, \sigma, etc.)
"""

from pathlib import Path
import re

VAULT_DIR = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me")
SCRATCH_DIR = Path("/Users/user/.gemini/antigravity-ide/scratch")

def fix_corrupted_latex(text: str) -> str:
    # 1. Substituir form feed seguido de rac por \frac
    text = text.replace("\x0crac", "\\frac")
    text = text.replace("\x0c", "\\f")
    
    # 2. Substituir tabs que corromperam comandos \text, \theta, \times, \tau, \top
    text = re.sub(r'\text(?=[a-zA-Z{_ ])', r'\\text', text)
    text = re.sub(r'\theta(?=[a-zA-Z{_ ,)\]$])', r'\\theta', text)
    text = re.sub(r'\times(?=[a-zA-Z{_ ,)\]$])', r'\\times', text)
    text = re.sub(r'\tau(?=[a-zA-Z{_ ,)\]$])', r'\\tau', text)
    text = re.sub(r'\top(?=[a-zA-Z{_ ,)\]$])', r'\\top', text)
    text = text.replace("\text{", "\\text{")
    text = text.replace("\theta", "\\theta")

    # 3. Substituir carriage returns e quebras em \right
    text = re.sub(r'[\r\n]+\s*ight', r'\\right', text)
    text = text.replace("\right", "\\right")
    text = text.replace("\rho", "\\rho")

    # 4. Substituir backspaces em \beta, \mathbf, \begin, \bar
    text = text.replace("\x08eta", "\\beta")
    text = text.replace("\x08mathbf", "\\mathbf")
    text = text.replace("\x08egin", "\\begin")
    text = text.replace("\x08ar", "\\bar")

    # 5. Comandos sem barra dentro de $...$
    # Ex: $sigma$ -> $\sigma$, $Delta_x$ -> $\Delta_x$, $alpha$ -> $\alpha$, $mu$ -> $\mu$
    def fix_inline_math(match):
        m = match.group(0)
        # Se contiver comandos comuns sem barra:
        replacements = [
            (r'(?<!\\)\bsigma\b', r'\\sigma'),
            (r'(?<!\\)\bDelta\b', r'\\Delta'),
            (r'(?<!\\)\balpha\b', r'\\alpha'),
            (r'(?<!\\)\bbeta\b', r'\\beta'),
            (r'(?<!\\)\bgamma\b', r'\\gamma'),
            (r'(?<!\\)\bmu\b', r'\\mu'),
            (r'(?<!\\)\btheta\b', r'\\theta'),
            (r'(?<!\\)\bcdot\b', r'\\cdot'),
            (r'(?<!\\)\bsum\b', r'\\sum'),
            (r'(?<!\\)\bint\b', r'\\int'),
            (r'(?<!\\)\biint\b', r'\\iint'),
            (r'(?<!\\)\bsqrt\b', r'\\sqrt'),
            (r'(?<!\\)\bleft\b', r'\\left'),
            (r'(?<!\\)\bright\b', r'\\right'),
            (r'(?<!\\)\bfrac\b', r'\\frac'),
            (r'(?<!\\)\btext\b', r'\\text'),
        ]
        for pat, rep in replacements:
            m = re.sub(pat, rep, m)
        return m

    text = re.sub(r'\$\$.*?\$\$', fix_inline_math, text, flags=re.DOTALL)
    text = re.sub(r'(?<!\$)\$(?!\$).*?(?<!\$)\$(?!\$)', fix_inline_math, text)

    # 6. Garantir que blocos $$ tenham quebra de linha apropriada para o MathJax do Obsidian
    def format_display_math(match):
        inner = match.group(1).strip()
        return f"\n$$\n{inner}\n$$\n"

    text = re.sub(r'\$\$(.*?)\$\$', format_display_math, text, flags=re.DOTALL)
    return text

def clean_all_notes():
    count = 0
    for base in [VAULT_DIR, SCRATCH_DIR]:
        for md_file in base.rglob("*.md"):
            try:
                original = md_file.read_text(encoding="utf-8")
                fixed = fix_corrupted_latex(original)
                if fixed != original:
                    md_file.write_text(fixed, encoding="utf-8")
                    count += 1
                    print(f"🔧 Corrigido LaTeX em: {md_file.relative_to(base)}")
            except Exception as e:
                print(f"Erro em {md_file}: {e}")
    print(f"✅ Total de notas corrigidas com LaTeX perfeito: {count}")

if __name__ == "__main__":
    clean_all_notes()
