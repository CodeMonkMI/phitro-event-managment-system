#!/bin/sh

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."

while ! python -c "import socket; s = socket.socket(); s.settimeout(1); s.connect(('evms_db', 5432)); s.close()" 2>/dev/null; do
  sleep 0.1
done

echo "PostgreSQL started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files echo "Collecting static files..." 
python manage.py collectstatic --noinput

echo "Collecting static files"

# Start Gunicorn server
echo "Starting Gunicorn..."
exec gunicorn evms.wsgi:application --bind 0.0.0.0:8000 --workers 3
