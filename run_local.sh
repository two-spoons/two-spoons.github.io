#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please run ./setup_local.sh first."
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if database exists, if not run migrations
if [ ! -f "db.sqlite3" ]; then
    echo "Database not found. Running migrations..."
    python manage.py makemigrations
    python manage.py migrate
fi

# Start the development server
echo "Starting Django development server..."
echo "Visit: http://127.0.0.1:8000"
echo "Admin panel: http://127.0.0.1:8000/admin"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver