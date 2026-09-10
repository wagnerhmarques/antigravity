import sys
import os
import re

sys.path.insert(0, "/Users/user/.gemini/antigravity-ide/scratch/pylibs")

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

md_path = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/TCC - Documento.md"
docx_path = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/TCC - Documento.docx"
assets_dir = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/assets"

doc = Document()

# --- 1. CONFIGURAÇÃO DE PÁGINA (ABNT NBR 14724 - Item 5.1) ---
# Formato A4, Margens: Superior 3cm, Esquerda 3cm, Inferior 2cm, Direita 2cm
for section in doc.sections:
    section.top_margin = Cm(3.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.0)
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    # Header and footer distance
    section.header_distance = Cm(2.0)
    section.footer_distance = Cm(1.5)

# --- 2. CONFIGURAÇÃO DE ESTILOS GLOBAIS (ABNT NBR 14724 - Item 5.2) ---
style_normal = doc.styles['Normal']
font = style_normal.font
font.name = 'Arial'
font.size = Pt(12)
font.color.rgb = RGBColor(0, 0, 0)
style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
style_normal.paragraph_format.line_spacing = 1.5
style_normal.paragraph_format.space_before = Pt(0)
style_normal.paragraph_format.space_after = Pt(0)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

# --- 3. ELEMENTOS PRÉ-TEXTUAIS PADRÃO ABNT NBR 14724 ---

# A) CAPA
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.0
p.paragraph_format.space_before = Pt(0)
p.paragraph_format.space_after = Pt(0)
r = p.add_run("UNIVERSIDADE DE SÃO PAULO\nINSTITUTO DE FÍSICA\nDEPARTAMENTO DE FÍSICA NUCLEAR\nCURSO DE BACHARELADO EM FÍSICA COM HABILITAÇÃO EM FÍSICA MÉDICA")
r.font.name = 'Arial'
r.font.size = Pt(12)
r.font.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.0
p.paragraph_format.space_before = Pt(100)
p.paragraph_format.space_after = Pt(0)
r = p.add_run("WAGNER H. M.")
r.font.name = 'Arial'
r.font.size = Pt(12)
r.font.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.5
p.paragraph_format.space_before = Pt(110)
p.paragraph_format.space_after = Pt(0)
r = p.add_run("MODELOS PERCEPTIVOS NA AVALIAÇÃO DA QUALIDADE DE IMAGEM EM TOMOGRAFIA COMPUTADORIZADA: DA TEORIA CLÁSSICA DE DETECÇÃO DE SINAIS AOS MODELOS DE APRENDIZADO PROFUNDO E OTIMIZAÇÃO MULTIOBJETIVO")
r.font.name = 'Arial'
r.font.size = Pt(12)
r.font.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.0
p.paragraph_format.space_before = Pt(140)
p.paragraph_format.space_after = Pt(0)
r = p.add_run("SÃO PAULO\n2026")
r.font.name = 'Arial'
r.font.size = Pt(12)
r.font.bold = True

doc.add_page_break()

# B) FOLHA DE ROSTO
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.0
p.paragraph_format.space_before = Pt(0)
p.paragraph_format.space_after = Pt(0)
r = p.add_run("WAGNER H. M.")
r.font.name = 'Arial'
r.font.size = Pt(12)
r.font.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.5
p.paragraph_format.space_before = Pt(100)
p.paragraph_format.space_after = Pt(0)
r = p.add_run("MODELOS PERCEPTIVOS NA AVALIAÇÃO DA QUALIDADE DE IMAGEM EM TOMOGRAFIA COMPUTADORIZADA: DA TEORIA CLÁSSICA DE DETECÇÃO DE SINAIS AOS MODELOS DE APRENDIZADO PROFUNDO E OTIMIZAÇÃO MULTIOBJETIVO")
r.font.name = 'Arial'
r.font.size = Pt(12)
r.font.bold = True

# Nota de apresentação ABNT (Recuo à esquerda de 8,0 cm, alinhamento justificado, fonte 10 pt, espaçamento simples)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.left_indent = Cm(8.0)
p.paragraph_format.space_before = Pt(60)
p.paragraph_format.space_after = Pt(0)
p.paragraph_format.line_spacing = 1.0
r = p.add_run(
    "Monografia de Conclusão de Curso apresentada ao Instituto de Física da Universidade de São Paulo, como parte dos requisitos necessários para a obtenção do título de Bacharel em Física com Habilitação em Física Médica.\n\n"
    "Orientador: Prof. Dr. Paulo Roberto Costa\n"
    "Área de Concentração: Física Médica e Radiológica"
)
r.font.name = 'Arial'
r.font.size = Pt(10)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.0
p.paragraph_format.space_before = Pt(100)
p.paragraph_format.space_after = Pt(0)
r = p.add_run("SÃO PAULO\n2026")
r.font.name = 'Arial'
r.font.size = Pt(12)
r.font.bold = True

doc.add_page_break()

# C) FOLHA DE APROVAÇÃO
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.0
p.paragraph_format.space_before = Pt(0)
p.paragraph_format.space_after = Pt(0)
r = p.add_run("FOLHA DE APROVAÇÃO\n\nWAGNER H. M.")
r.font.name = 'Arial'
r.font.size = Pt(12)
r.font.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.line_spacing = 1.5
p.paragraph_format.space_before = Pt(20)
p.paragraph_format.space_after = Pt(0)
r = p.add_run("Modelos Perceptivos na Avaliação da Qualidade de Imagem em Tomografia Computadorizada: Da Teoria Clássica de Detecção de Sinais aos Modelos de Aprendizado Profundo e Otimização Multiobjetivo")
r.font.name = 'Arial'
r.font.size = Pt(12)
r.font.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
p.paragraph_format.left_indent = Cm(8.0)
p.paragraph_format.space_before = Pt(30)
p.paragraph_format.space_after = Pt(30)
p.paragraph_format.line_spacing = 1.0
r = p.add_run("Monografia de Conclusão de Curso defendida e aprovada em _____ de ________________ de 2026 pela banca examinadora constituída pelos seguintes membros:")
r.font.name = 'Arial'
r.font.size = Pt(10)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(20)
p.paragraph_format.space_after = Pt(0)
p.paragraph_format.line_spacing = 1.5
r = p.add_run(
    "____________________________________________________\n"
    "Prof. Dr. Paulo Roberto Costa (Orientador / Presidente)\n"
    "Instituto de Física da Universidade de São Paulo – IFUSP\n\n\n"
    "____________________________________________________\n"
    "Membro da Banca Examinadora 1\n"
    "Instituto de Radiologia do Hospital das Clínicas – InRad-HCFMUSP\n\n\n"
    "____________________________________________________\n"
    "Membro da Banca Examinadora 2\n"
    "Instituto de Física da Universidade de São Paulo – IFUSP"
)
r.font.name = 'Arial'
r.font.size = Pt(10)

doc.add_page_break()

# --- 4. CORPO DO TRABALHO E DEMAIS SEÇÕES ---
with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

# Start from RESUMO
start_idx = 0
for idx, l in enumerate(lines):
    if l.strip().startswith('## RESUMO') or l.strip().startswith('# RESUMO'):
        start_idx = idx
        break

i = start_idx
in_table = False
table_lines = []
in_math_block = False
math_lines = []

while i < len(lines):
    line = lines[i].strip()

    if line == '---':
        i += 1
        continue

    # Math block $$ ... $$
    if line.startswith('$$') and line.endswith('$$') and len(line) > 2:
        math_content = line[2:-2].strip()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(8)
        run = p.add_run(math_content)
        run.font.name = 'Cambria Math'
        run.font.size = Pt(11.5)
        run.font.italic = True
        run.font.color.rgb = RGBColor(0, 51, 102)
        i += 1
        continue
    elif line == '$$':
        if in_math_block:
            in_math_block = False
            math_content = "\n".join(math_lines)
            math_lines = []
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(8)
            run = p.add_run(math_content)
            run.font.name = 'Cambria Math'
            run.font.size = Pt(11.5)
            run.font.italic = True
            run.font.color.rgb = RGBColor(0, 51, 102)
        else:
            in_math_block = True
            math_lines = []
        i += 1
        continue
    elif in_math_block:
        math_lines.append(line)
        i += 1
        continue

    # Table handling
    if line.startswith('|') and line.endswith('|'):
        table_lines.append(line)
        in_table = True
        i += 1
        continue
    else:
        if in_table:
            rows_data = []
            for tline in table_lines:
                if re.match(r'\|[\s\-:]+\|', tline):
                    continue
                cells = [c.strip() for c in tline.strip('|').split('|')]
                rows_data.append(cells)
            
            if rows_data:
                num_cols = max(len(r) for r in rows_data)
                tbl = doc.add_table(rows=len(rows_data), cols=num_cols)
                tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                set_table_borders(tbl)
                for r_idx, r_data in enumerate(rows_data):
                    row = tbl.rows[r_idx]
                    is_header = (r_idx == 0)
                    for c_idx in range(num_cols):
                        cell = row.cells[c_idx]
                        cell_text = r_data[c_idx] if c_idx < len(r_data) else ""
                        cell_text = re.sub(r'\*\*(.*?)\*\*', r'\1', cell_text)
                        cell.text = cell_text
                        p = cell.paragraphs[0]
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        p.paragraph_format.line_spacing = 1.0
                        p.paragraph_format.space_before = Pt(4)
                        p.paragraph_format.space_after = Pt(4)
                        for r in p.runs:
                            r.font.name = 'Arial'
                            r.font.size = Pt(10)
                            if is_header:
                                r.font.bold = True
                                r.font.color.rgb = RGBColor(0, 0, 0)
                        if is_header:
                            set_cell_background(cell, "EAEAEA")
                        elif r_idx % 2 == 1:
                            set_cell_background(cell, "FAFAFA")
                doc.add_paragraph().paragraph_format.space_after = Pt(6)
            table_lines = []
            in_table = False

    # Chapter / Primary Heading (NBR 6024: 1 INTRODUÇÃO - Caixa Alta, Negrito, 12pt, quebra de página)
    if line.startswith('# ') or line.startswith('## RESUMO') or line.startswith('## ABSTRACT') or line.startswith('## LISTA') or line.startswith('# SUMÁRIO'):
        heading_text = re.sub(r'^#+\s*', '', line).strip()
        
        # Add page break before major chapters / pre-textual sections (except Resumo which starts right after Folha de Aprovação)
        if not line.startswith('## RESUMO'):
            doc.add_page_break()

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(12)
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(heading_text.upper())
        run.font.name = 'Arial'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        i += 1
        continue

    # Secondary Heading (NBR 6024: 1.1 TÍTULO - Caixa Alta, sem negrito, 12pt)
    if line.startswith('## ') and not line.startswith('## RESUMO') and not line.startswith('## ABSTRACT') and not line.startswith('## LISTA'):
        heading_text = line[3:].strip()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(12)
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(heading_text)
        run.font.name = 'Arial'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        i += 1
        continue

    # Tertiary Heading (NBR 6024: 1.1.1 Título - Caixa Baixa, Negrito, 12pt)
    if line.startswith('### '):
        heading_text = line[4:].strip()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(heading_text)
        run.font.name = 'Arial'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        i += 1
        continue

    # Quaternary Heading (NBR 6024: 1.1.1.1 Título - Caixa Baixa, Itálico, 12pt)
    if line.startswith('#### '):
        heading_text = line[5:].strip()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(heading_text)
        run.font.name = 'Arial'
        run.font.size = Pt(12)
        run.font.italic = True
        run.font.color.rgb = RGBColor(0, 0, 0)
        i += 1
        continue

    # Image handling: ![Caption](assets/image.png)
    img_match = re.match(r'!\[(.*?)\]\((assets/.*?)\)', line)
    if img_match:
        caption = img_match.group(1)
        img_rel_path = img_match.group(2)
        img_full_path = os.path.join(os.path.dirname(md_path), img_rel_path)
        if os.path.exists(img_full_path):
            # Top Caption (ABNT: Tipo e número em cima)
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.line_spacing = 1.0
            p_cap.paragraph_format.space_before = Pt(12)
            p_cap.paragraph_format.space_after = Pt(4)
            p_cap.paragraph_format.first_line_indent = Cm(0)
            p_cap.paragraph_format.keep_with_next = True
            r_cap = p_cap.add_run(caption)
            r_cap.font.name = 'Arial'
            r_cap.font.size = Pt(10)
            r_cap.font.bold = True

            # Picture
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(2)
            p_img.paragraph_format.space_after = Pt(2)
            p_img.paragraph_format.first_line_indent = Cm(0)
            p_img.paragraph_format.keep_with_next = True
            run = p_img.add_run()
            run.add_picture(img_full_path, width=Inches(6.0))
            
            # Bottom Source (ABNT: Fonte embaixo, tamanho 10pt)
            p_src = doc.add_paragraph()
            p_src.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_src.paragraph_format.line_spacing = 1.0
            p_src.paragraph_format.space_before = Pt(2)
            p_src.paragraph_format.space_after = Pt(12)
            p_src.paragraph_format.first_line_indent = Cm(0)
            r_src = p_src.add_run("Fonte: Elaborado pelo autor (2026).")
            r_src.font.name = 'Arial'
            r_src.font.size = Pt(10)
        i += 1
        continue

    # Skip duplicate sources
    if line.startswith('Fonte:') or line.startswith('Figura') or line.startswith('Fluxograma') or line.startswith('Quadro') or line.startswith('Tabela'):
        if 'Elaborado pelo autor' in line:
            i += 1
            continue

    if not line:
        i += 1
        continue

    # Lists - Bullet and Numbered (ABNT: Justificado, 1,5 entre linhas)
    if line.startswith('- ') or line.startswith('* '):
        item_text = line[2:].strip()
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        
        parts = re.split(r'(\*\*.*?\*\*|\*.*?\*|\$.*?\$)', item_text)
        for part in parts:
            if not part: continue
            if part.startswith('**') and part.endswith('**'):
                r = p.add_run(part[2:-2])
                r.font.bold = True
            elif part.startswith('*') and part.endswith('*'):
                r = p.add_run(part[1:-1])
                r.font.italic = True
            elif part.startswith('$') and part.endswith('$'):
                r = p.add_run(part[1:-1])
                r.font.italic = True
                r.font.name = 'Cambria Math'
            else:
                p.add_run(part)
        i += 1
        continue

    if re.match(r'^(\d+\.|\w\))\s+', line):
        match = re.match(r'^(\d+\.|\w\))\s+', line)
        prefix = match.group(0)
        item_text = line[len(prefix):].strip()
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.25)
        p.paragraph_format.first_line_indent = Cm(-1.25)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        r_pre = p.add_run(prefix)
        r_pre.font.bold = True
        
        parts = re.split(r'(\*\*.*?\*\*|\*.*?\*|\$.*?\$)', item_text)
        for part in parts:
            if not part: continue
            if part.startswith('**') and part.endswith('**'):
                r = p.add_run(part[2:-2])
                r.font.bold = True
            elif part.startswith('*') and part.endswith('*'):
                r = p.add_run(part[1:-1])
                r.font.italic = True
            elif part.startswith('$') and part.endswith('$'):
                r = p.add_run(part[1:-1])
                r.font.italic = True
                r.font.name = 'Cambria Math'
            else:
                p.add_run(part)
        i += 1
        continue

    # Body Paragraph (ABNT: Justificado, 1,5 entre linhas, recuo de 1,25 cm na 1ª linha)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)

    # Bibliographic References (NBR 6023: Alinhamento à esquerda, espaçamento simples, sem recuo, espaço de 6pt depois)
    if re.match(r'^[A-ZÁÉÍÓÚÇ]{3,}', line) and (', ' in line or ' (' in line):
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_after = Pt(6)

    # Resumo / Abstract keywords (NBR 6028: Sem recuo de primeira linha)
    if 'Palavras-chave:' in line or 'Keywords:' in line:
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(0)

    # Parse inline formatting
    parts = re.split(r'(\*\*.*?\*\*|\*.*?\*|\$.*?\$)', line)
    for part in parts:
        if not part: continue
        if part.startswith('**') and part.endswith('**'):
            r = p.add_run(part[2:-2])
            r.font.bold = True
        elif part.startswith('*') and part.endswith('*'):
            r = p.add_run(part[1:-1])
            r.font.italic = True
        elif part.startswith('$') and part.endswith('$'):
            r = p.add_run(part[1:-1])
            r.font.italic = True
            r.font.name = 'Cambria Math'
        else:
            p.add_run(part)

    i += 1

doc.save(docx_path)
print(f"Strict ABNT formatting successfully applied to {docx_path}")
print(f"File size: {os.path.getsize(docx_path)} bytes")
