import re
import json

def robust_parse_json(raw_text: str):
    text = raw_text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    # Pre-process unescaped backslashes inside JSON strings
    # We want any backslash that is part of LaTeX (like \frac, \text, \Delta, \sigma, \int, etc.)
    # to be doubled so json.loads parses it as a literal '\frac' instead of control chars or error.
    
    # In JSON, valid escape characters are: \", \\, \/, \b, \f, \n, \r, \t, \uXXXX
    # But in markdown with LaTeX:
    # \f -> \frac, \forall
    # \t -> \text, \theta, \times, \tau, \top
    # \r -> \right, \rho, \rangle
    # \b -> \beta, \mathbf, \boldsymbol, \begin, \bar, \big
    # \n -> \nabla, \nu, \neq, \newcommand, \null
    # All of these are LaTeX commands!
    
    # Let's inspect: When Gemini returns JSON, it writes text with newlines either as literal newlines or \n.
    # If we convert every single backslash that is NOT followed by " (quote) or another backslash into \\:
    # Specifically:
    # Any backslash followed by letters (e.g. \frac, \text, \sum) -> \\frac, \\text, \\sum
    # Any backslash followed by { or } or | or ; or , or . or ! -> \\{, \\}, \\|, etc.
    # Any backslash followed by whitespace or other non-quote chars -> double it.
    
    def replace_backslashes(match):
        content = match.group(0)
        # We are inside a JSON string
        # Double backslashes that aren't escaping quotes
        # Replace \ followed by anything other than " or \ with \\ + char
        # But handle \n and \r and \t: in LaTeX text, we want literal \n (or real newline)
        pass

    # A very clean method:
    # 1. Protect valid \" and \\ by replacing them with placeholders
    s = text.replace('\\\\', '__DOUBLE_BACKSLASH__')
    s = s.replace('\\"', '__ESCAPED_QUOTE__')
    
    # 2. Now, any remaining backslash '\' in the string is an unescaped backslash (like \frac, \text, \Delta, \n, \t)
    # If we want them to be literal LaTeX backslashes:
    # Double every remaining backslash!
    s = s.replace('\\', '\\\\')
    
    # 3. Restore protected sequences
    s = s.replace('__ESCAPED_QUOTE__', '\\"')
    s = s.replace('__DOUBLE_BACKSLASH__', '\\\\\\\\')

    # Now parse with json.loads
    try:
        data = json.loads(s, strict=False)
        return data
    except Exception as e:
        # Fallback with json5 or relaxed parser
        import json5
        return json5.loads(s)

# Test cases
test_gemini_output = r'''{
  "titulo": "Teste de LaTeX",
  "formula_display": "$$NPS_{2D}(f_x, f_y) = \frac{\Delta_x \Delta_y}{L_x L_y} \cdot \frac{1}{N_{ROI}} \sum_{i=1}^{N_{ROI}} \left| \text{FFT}_{2D} \left\{ \text{ROI}_i(x,y) - \text{FIT}_i(x,y) \right\} \right|^2$$",
  "inline": "O desvio padrão é $\sigma$ e o ângulo é $\theta$ e a frequência $\nu$ e $\beta$",
  "texto_com_linhas": "Primeira linha.\nSegunda linha."
}'''

parsed = robust_parse_json(test_gemini_output)
print("=== PARSED RESULT ===")
print("formula_display:", repr(parsed["formula_display"]))
print("inline:", repr(parsed["inline"]))
print("\n--- Display Render Check ---")
print(parsed["formula_display"])
print(parsed["inline"])
