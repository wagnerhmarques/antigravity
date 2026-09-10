import os
import shutil
import zipfile

base_dir = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/Overleaf_TCC"
os.makedirs(base_dir, exist_ok=True)
os.makedirs(os.path.join(base_dir, "config"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "tex"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "figuras"), exist_ok=True)

# Copy figures
src_assets = "/Users/user/Library/Mobile Documents/iCloud~md~obsidian/Documents/Me/USP/assets"
for img in os.listdir(src_assets):
    if img.endswith(".png"):
        shutil.copy2(os.path.join(src_assets, img), os.path.join(base_dir, "figuras", img))

# Copy relatese.sty and Makefile
shutil.copy2("/Users/user/.gemini/antigravity-ide/scratch/template_extracted/relatese.sty", os.path.join(base_dir, "relatese.sty"))
shutil.copy2("/Users/user/.gemini/antigravity-ide/scratch/template_extracted/Makefile", os.path.join(base_dir, "Makefile"))

# Copy config/preamble.tex
shutil.copy2("/Users/user/.gemini/antigravity-ide/scratch/template_extracted/config/preamble.tex", os.path.join(base_dir, "config", "preamble.tex"))

# Copy references.bib
shutil.copy2("/Users/user/.gemini/antigravity-ide/scratch/build_bib.py", "/tmp/dummy.py")
os.system("python3 /Users/user/.gemini/antigravity-ide/scratch/build_bib.py")
os.system("python3 /Users/user/.gemini/antigravity-ide/scratch/build_tex_chapters.py")
os.system("python3 /Users/user/.gemini/antigravity-ide/scratch/build_fundamentacao_tex.py")
os.system("python3 /Users/user/.gemini/antigravity-ide/scratch/build_metodos_tex.py")
os.system("python3 /Users/user/.gemini/antigravity-ide/scratch/build_remaining_tex.py")
os.system("python3 /Users/user/.gemini/antigravity-ide/scratch/build_ultra_fast_zip.py")

print("Full Overleaf package generated and zipped!")
