#!/usr/bin/env bash

until cd /app/
do
    echo "Waiting for django volume..."
done

echo "Running migration..."
python3 manage.py migrate --noinput