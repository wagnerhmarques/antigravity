import re
import os

base_dir = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/Overleaf_TCC"

# Check references keys
with open(os.path.join(base_dir, "references.bib"), "r") as f:
    bib = f.read()

bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib))
print("Total bib keys defined:", len(bib_keys))

# Check citations in all tex files
missing_keys = set()
used_keys = set()

tex_dir = os.path.join(base_dir, "tex")
for tex_file in os.listdir(tex_dir):
    if tex_file.endswith(".tex"):
        with open(os.path.join(tex_dir, tex_file), "r") as f:
            content = f.read()
        cites = re.findall(r'\\supercite\{([^}]+)\}', content)
        for c in cites:
            for k in c.split(","):
                k = k.strip()
                used_keys.add(k)
                if k not in bib_keys:
                    missing_keys.add((tex_file, k))

print("Total unique keys used:", len(used_keys))
if missing_keys:
    print("WARNING: Missing bib keys:", missing_keys)
else:
    print("SUCCESS: All cited keys are present in references.bib!")

# Check figures referenced
fig_dir = os.path.join(base_dir, "figuras")
available_figs = set(os.listdir(fig_dir))
missing_figs = set()
for tex_file in os.listdir(tex_dir):
    if tex_file.endswith(".tex"):
        with open(os.path.join(tex_dir, tex_file), "r") as f:
            content = f.read()
        figs = re.findall(r'\\includegraphics(?:\[.*?\])?\{figuras/(.*?)\}', content)
        for fig in figs:
            if fig not in available_figs:
                missing_figs.add((tex_file, fig))

if missing_figs:
    print("WARNING: Missing figures:", missing_figs)
else:
    print("SUCCESS: All referenced figures exist in figuras/ folder!")
