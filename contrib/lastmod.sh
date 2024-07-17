#!/bin/sh

sed -i 's/lastmod: .*/lastmod: '"$(date +'%Y-%m-%d')"'/g' "$1"
