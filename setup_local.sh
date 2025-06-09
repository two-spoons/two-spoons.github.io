#!/bin/bash

echo "Setting up Django Blog for local development..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3."
    exit 1
fi

# We'll use python -m pip to avoid pip installation issues

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Run migrations
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if requested
read -p "Do you want to create a superuser? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Creating superuser..."
    python manage.py createsuperuser
fi

echo ""
echo "Setup complete!"
echo ""
echo "To start the development server:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Start the server: python manage.py runserver"
echo "3. Visit: http://127.0.0.1:8000"
echo "4. Admin panel: http://127.0.0.1:8000/admin"
echo ""