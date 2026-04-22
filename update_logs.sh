#!/bin/bash
# Sync structured logs from sandbox/details.json to website/logs.json
SOURCE="/home/q/.openclaw/workspace/sandbox/details.json"
DEST="/home/q/.openclaw/workspace/website/logs.json"

if [ ! -f "$SOURCE" ]; then
    echo "[]" > "$DEST"
    exit 0
fi

cp "$SOURCE" "$DEST"
