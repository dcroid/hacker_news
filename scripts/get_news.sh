#!/usr/bin/env bash
until cd /app/
do
    echo "Waiting for django volume..."
done

echo "Running Spider..."
python3 manage.py get_news
