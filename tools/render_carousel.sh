#!/usr/bin/env bash
# Render a carousel HTML (slides of 1080x1350) to a LinkedIn-ready PDF.
# Usage: tools/render_carousel.sh <input.html> <output.pdf>
set -euo pipefail

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
input="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
output="$2"

"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=5000 \
  --print-to-pdf="$output" "file://$input" 2>/dev/null
echo "PDF: $output"
