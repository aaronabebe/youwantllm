#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate
gunicorn config.wsgi --bind=0.0.0.0:80 --workers 4