#!/bin/bash

while ! nc -z db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py db migrate

python manage.py db upgrade

gunicorn --workers 3 --bind 0.0.0.0:8000 manage:app