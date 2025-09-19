#!/usr/bin/env bash
# Serve the site locally with incremental rebuilds and live reload.
set -euo pipefail
bundle exec jekyll serve --livereload --incremental "$@"
