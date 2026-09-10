with open('/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/TCC - Documento.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_code = False
code_blocks = []
current_block = []
start_idx = 0

for idx, line in enumerate(lines):
    if line.strip().startswith('```'):
        if in_code:
            code_blocks.append((start_idx, idx, ''.join(current_block)))
            current_block = []
            in_code = False
        else:
            in_code = True
            start_idx = idx
    elif in_code:
        current_block.append(line)

print(f'Total code blocks found: {len(code_blocks)}')
for s, e, content in code_blocks:
    print(f'=== Block lines {s+1} to {e+1} ===')
    print(content)
