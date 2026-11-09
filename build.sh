
#!/usr/bin/env bash

set -o errexit

# Install project dependencies
pip install -r requirements.txt

# Collect CSS, JavaScript and other static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
