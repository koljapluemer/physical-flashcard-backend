#!/usr/bin/env bash
set -o errexit

# Install dependencies via uv (locked, main deps only)
uv sync --no-dev --frozen

# Run management commands inside uv-managed environment
uv run python manage.py collectstatic --no-input
uv run python manage.py migrate
