#!/bin/bash
# Render every batch1 script (dry run) and copy the mp4s to the desktop.
cd "$(dirname "$0")/.." || exit 1
export PYTHONIOENCODING=utf-8
DEST="$HOME/Desktop/Chismepón 1차"
mkdir -p "$DEST"
for f in batch1/[0-9][0-9]-*.json; do
  n=$(basename "$f" .json)
  echo "=== $n $(date +%T)"
  python run.py --script "$f" --dry-run --slot 1200 --date 2026-10-13 2>&1 | grep -E "stock clips|duration|Error|error|Traceback" | tail -5
  slug=$(python -c "import json,sys; print(json.load(open(sys.argv[1],encoding='utf-8'))['slug'])" "$f")
  cp "output/2026-10-13_1200_${slug}/video.mp4" "$DEST/${n}.mp4" && echo "  -> $DEST/${n}.mp4"
done
echo "ALL DONE $(date +%T)"
