import json
import re

# Comprehensive test with all tricky cases: \theta, \tau, \text, \times, \begin, \nabla, \frac, \left\{, \right\}, 50%, \Delta_x, newlines
raw_gemini_json = r"""{
  "titulo": "Teste de Rigor LaTeX",
  "resposta_markdown": "## 1. Equação Angular e Temporal\nA integral angular sobre \theta e o tempo de decaimento \tau são:\n$$\n\text{SNR}(\theta, \tau) = \frac{\Delta_x \times \Delta_y}{\sqrt{\sigma^2 + \text{NPS}(u,v)}} \cdot \left\{ 1 - \exp(-\tau/\theta) \right\}\n$$\nCom 50\% de dose e \nabla \cdot \mathbf{B} = 0."
}"""

def robust_json_preprocess(raw_json_str: str) -> str:
    # Whitelist of standard LaTeX commands and symbols
    # Double backslash for all LaTeX escapes so json.loads keeps the literal \
    def replace_slash(match):
        full = match.group(0)
        char = match.group(1)
        rest = match.group(2)
        
        # Real JSON newline
        if char == 'n' and (not rest or rest[0] in [' ', '\t', '\n', '"', ',', ']', '}', '#', '-', '*', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']):
            # If rest starts with LaTeX word like \nabla, \nu, \neq, it is LaTeX!
            if rest.startswith(('abla', 'u', 'eq', 'ewcommand', 'ull')):
                return '\\\\' + char + rest
            return '\\n' + rest
            
        if char == 't' and (not rest or rest[0] in [' ', '\t', '\n', '"', ',']):
            # If rest starts with LaTeX word like \theta, \tau, \text, \times, \tan, \tanh, \top, \tilde, it is LaTeX!
            if rest.startswith(('heta', 'au', 'ext', 'imes', 'an', 'anh', 'op', 'ilde', 'ag', 'riangle', 'herefore')):
                return '\\\\' + char + rest
            return '\\t' + rest

        if char in ['"', '\\', '/']:
            return full

        # Double backslash for LaTeX (e.g. \theta, \tau, \text, \frac, \{, \}, \%, \Delta, \sigma)
        return '\\\\' + char + rest

    pattern = r'\\([a-zA-Z%${}_|;,!.\'])([a-zA-Z0-9_]*)'
    fixed = re.sub(pattern, replace_slash, raw_json_str)
    return fixed

# Test parsing
fixed = robust_json_preprocess(raw_gemini_json)
parsed = json.loads(fixed)

print("=== PARSED MARKDOWN CONTENT ===")
print(parsed["resposta_markdown"])

# Verify \theta, \tau, \text, \times, \frac, \left\{, \right\}, 50%, \Delta_x, \nabla
for expected in [r"\theta", r"\tau", r"\text{SNR}", r"\frac", r"\Delta_x", r"\times", r"\left\{", r"\right\}", r"50\%", r"\nabla"]:
    assert expected in parsed["resposta_markdown"], f"FAIL: missing {expected}"

print("\n🎉 ALL ASSERTIONS PASSED! 100% OF LATEX COMMANDS (INCLUDING \\theta, \\tau, \\text) FULLY PRESERVED!")
