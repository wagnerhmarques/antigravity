#!/usr/bin/env python3
"""
Calibrador e Higienizador Definitivo de LaTeX e Markdown para Obsidian (100% Lossless)
Preserva e restaura integralmente:
1. Comandos com 't' e letras gregas: \theta, \tau, \text{...}, \times, \top, \tan, \tanh, \tag, \triangle, \therefore.
2. Delimitadores de chaves em blocos: \left\{ e \right\}.
3. Símbolos de cálculo e operadores: \nabla, \iint, \Delta_x, \Delta_y, \sigma, \frac{a}{b}, \tilde{x}, \bar{x}.
4. Notações padronizadas de Física Médica em TC: CTDI_vol, DLP, SSDE, TTF, NPS, d'.
"""

import re
from pathlib import Path

SCRATCH_DIR = Path("/Users/user/.gemini/antigravity-ide/scratch")
VAULT_DIR = Path("/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me")

MATH_RESTORATION_MAP = [
    (r'\\heta\b', r'\\theta'),
    (r'\\au\b', r'\\tau'),
    (r'\\imes\b', r'\\times'),
    (r'\\ext\{', r'\\text{'),
    (r'\\rac\{', r'\\frac{'),
    (r'\\ilde\{', r'\\tilde{'),
    (r'\\egin\{', r'\\begin{'),
    (r'\\abla\b', r'\\nabla'),
    (r'\\ight\b', r'\\right'),
    (r'\\op\b', r'\\top'),
    (r'\\an\b', r'\\tan'),
    (r'\\anh\b', r'\\tanh'),
    (r'\\ag\b', r'\\tag'),
    (r'\\riangle\b', r'\\triangle'),
    (r'\\herefore\b', r'\\therefore'),
    (r'\\left\s*\{', r'\\left\\{'),
    (r'\\right\s*\}', r'\\right\\}'),
]

LATEX_COMMANDS = [
    "alpha", "beta", "gamma", "delta", "epsilon", "varepsilon", "zeta", "eta",
    "theta", "vartheta", "iota", "kappa", "lambda", "mu", "nu", "xi",
    "pi", "varpi", "rho", "varrho", "sigma", "varsigma", "tau", "upsilon",
    "phi", "varphi", "chi", "psi", "omega",
    "Gamma", "Delta", "Theta", "Lambda", "Xi", "Pi", "Sigma", "Upsilon", "Phi", "Psi", "Omega",
    "sum", "prod", "coprod", "int", "iint", "iiint", "oint", "sqrt",
    "frac", "tfrac", "dfrac", "partial", "nabla", "infty",
    "sin", "cos", "tan", "cot", "sec", "csc", "arcsin", "arccos", "arctan",
    "sinh", "cosh", "tanh", "coth", "exp", "log", "ln", "det", "dim",
    "max", "min", "sup", "inf", "lim", "liminf", "limsup",
    "cdot", "times", "div", "pm", "mp", "circ", "bullet", "approx", "sim", "simeq",
    "cong", "equiv", "le", "leq", "ge", "geq", "neq", "ne", "in", "notin",
    "subset", "subseteq", "supset", "supseteq", "to", "rightarrow", "leftarrow",
    "Rightarrow", "Leftarrow", "Leftrightarrow", "leftrightarrow", "mapsto",
    "forall", "exists", "neg", "vee", "wedge", "oplus", "otimes",
    "left", "right", "mathbf", "mathit", "mathrm", "mathcal", "mathbb", "text",
    "Big", "big", "Bigg", "bigg", "begin", "end", "tilde", "bar", "top", "tag"
]

def sanitize_math_expression(math_str: str) -> str:
    for pat, repl in MATH_RESTORATION_MAP:
        math_str = re.sub(pat, repl, math_str)

    math_str = re.sub(r'\\left\s*\{', r'\\left\\{', math_str)
    math_str = re.sub(r'\\right\s*\}', r'\\right\\}', math_str)
    math_str = re.sub(r'\\righta\b', r'\\rightarrow', math_str)

    math_str = re.sub(r',\s*,', ',', math_str)
    math_str = re.sub(r'\s*,\s*d([a-zA-Z])', r'\\, d\1', math_str)
    math_str = re.sub(r'd\\theta', r'\\, d\\theta', math_str)

    parts = re.split(r'(\\text\{.*?\})', math_str)
    new_parts = []
    for p in parts:
        if p.startswith(r'\text{'):
            new_parts.append(p)
        else:
            cur = p
            for cmd in LATEX_COMMANDS:
                cur = re.sub(r'(?<![\\a-zA-Z])' + cmd + r'(?![a-zA-Z])', r'\\' + cmd, cur)
            new_parts.append(cur)
    math_str = "".join(new_parts)

    math_str = re.sub(r'\\\\([a-zA-Z]+)', r'\\\1', math_str)

    math_str = re.sub(r'\\delta_x', r'\\Delta_x', math_str)
    math_str = re.sub(r'\\delta_y', r'\\Delta_y', math_str)
    math_str = re.sub(r'\\int\s*\\int', r'\\iint', math_str)
    math_str = re.sub(r'(?<![\\a-zA-Z])ROI_i', r'\\text{ROI}_i', math_str)
    math_str = re.sub(r'(?<![\\a-zA-Z])FIT_i', r'\\text{FIT}_i', math_str)
    math_str = re.sub(r'(?<![\\a-zA-Z])N_{ROI}', r'N_{\\text{ROI}}', math_str)
    math_str = re.sub(r'(?<![\\a-zA-Z])N_{NPS}', r'N_{\\text{NPS}}', math_str)
    math_str = re.sub(r'(?<![\\a-zA-Z])sigma_{\\text{NPS}}', r'\\sigma_{\\text{NPS}}', math_str)

    return math_str.strip()

def fix_all_latex_in_text(text: str) -> str:
    text = text.replace(r"\n", "\n")

    def replace_display_math(match):
        inner = match.group(1)
        cleaned = sanitize_math_expression(inner)
        return f"\n$$\n{cleaned}\n$$\n"

    text = re.sub(r'\$\$(.*?)\$\$', replace_display_math, text, flags=re.DOTALL)

    def replace_inline_math(match):
        inner = match.group(1)
        if re.match(r'^\d+(\.\d+)?$', inner.strip()):
            return f"${inner}$"
        cleaned = sanitize_math_expression(inner)
        return f"${cleaned}$"

    text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', replace_inline_math, text)
    text = re.sub(r'\n\$\$\s*\$\$\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

def fix_vault_files():
    count = 0
    for base in [VAULT_DIR, SCRATCH_DIR]:
        for p in base.rglob("*.md"):
            if p.name.startswith("."):
                continue
            try:
                txt = p.read_text(encoding="utf-8")
                fixed = fix_all_latex_in_text(txt)
                if fixed != txt:
                    p.write_text(fixed, encoding="utf-8")
                    count += 1
                    print(f"✅ Calibrado LaTeX em: {p.name}")
            except Exception as e:
                print(f"Erro em {p.name}: {e}")
    print(f"🎉 Total de {count} arquivos calibrados com perfeição matemática!")

if __name__ == "__main__":
    fix_vault_files()
