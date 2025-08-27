#!/usr/bin/env bash
set -euo pipefail

# Simple script to generate DEPLOYMENT.pdf locally using pandoc
# Requirements: pandoc, texlive-xetex

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not installed. Install it with: sudo apt install pandoc"
  exit 1
fi

pandoc DEPLOYMENT.md -o DEPLOYMENT.pdf --pdf-engine=xelatex --metadata title="PyPI Deployment Guide" --resource-path=DEPLOYMENT-images

echo "Generated DEPLOYMENT.pdf"
