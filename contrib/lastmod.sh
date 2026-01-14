#!/bin/sh

for file in "$@"; do
    if echo "$file" | grep -q "content/anotacoes/Weeknotes/"; then
        # For Weeknotes, extract the end date from filename (e.g., "2025-01-04 - 2025-01-10.md")
        lastmod=$(basename "$file" .md | sed 's/.* - //')
    else
        # For other files, use today's date
        lastmod=$(date +'%Y-%m-%d')
    fi
    sed -i 's/lastmod: .*/lastmod: '"$lastmod"'/g' "$file"
done
