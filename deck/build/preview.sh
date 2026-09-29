#!/usr/bin/env bash
# Renders the deck to PDF + PNGs for visual QA. Usage: ./preview.sh <outdir>
set -euo pipefail
OUT="${1:?usage: preview.sh <outdir>}"
SK="${PPTX_SKILL:?set PPTX_SKILL to the pptx skill directory}"
DECK="$(cd "$(dirname "$0")/.." && pwd)/Nemoire_SIH26063.pptx"
mkdir -p "$OUT"
rm -f "${OUT:?}"/Nemoire_SIH26063.pdf "${OUT:?}"/slide-*.png
python3 "$SK/scripts/office/soffice.py" --headless --convert-to pdf --outdir "$OUT" "$DECK" 2>&1 | grep -v javaldx || true
python3 - "$OUT" <<'EOF'
import sys, pymupdf
out = sys.argv[1]
d = pymupdf.open(f"{out}/Nemoire_SIH26063.pdf")
for i, p in enumerate(d):
    p.get_pixmap(dpi=144).save(f"{out}/slide-{i+1}.png")
print("pages:", len(d), "fonts:", sorted({f[3] for p in d for f in p.get_fonts()}))
EOF
