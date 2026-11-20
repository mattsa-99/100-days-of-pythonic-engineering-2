#!/usr/bin/env bash
# Render a day's carousel to PDF (one page per slide, 1080x1350) and PNG previews.
# Usage: scripts/render.sh days/day04_data_skew pino
set -euo pipefail

DAY_DIR="$1"
THEME="$2"
NAME="$(basename "$DAY_DIR")"
CHROME="${CHROME:-$(command -v google-chrome || command -v chromium || command -v chromium-browser || echo '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')}"

python3 "$DAY_DIR/build.py" "$THEME" "$DAY_DIR/$NAME.html"
"$CHROME" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$DAY_DIR/$NAME.pdf" "file://$(cd "$DAY_DIR" && pwd)/$NAME.html"

mkdir -p "$DAY_DIR/preview"
if command -v pdftoppm >/dev/null; then
  pdftoppm -png -r 72 "$DAY_DIR/$NAME.pdf" "$DAY_DIR/preview/slide"
elif command -v swift >/dev/null; then
  # macOS fallback without Poppler: same preview/slide-N.png output via PDFKit
  swift "$(dirname "$0")/preview_pdf.swift" "$DAY_DIR/$NAME.pdf" "$DAY_DIR/preview"
fi
echo "OK -> $DAY_DIR/$NAME.pdf"
