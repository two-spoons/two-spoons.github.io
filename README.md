# two_spoons_online

A Django blog application with categories for Writing, Casting, and Coding, featuring a Dracula theme and Input Mono font.

## Features

- **Categories**: Writing, Casting, Coding
- **Theme**: Dracula color scheme with lowercase text
- **Font**: Input Mono monospaced font
- **Responsive**: Bootstrap-based responsive design
- **Admin**: Django admin interface for content management

## Development

### Prerequisites

- Python 3.11+
- pip

### Local Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd twospoonsanewhope
   ```

2. Run the setup script:
   ```bash
   ./setup_local.sh
   ```

3. Start the development server:
   ```bash
   ./run_local.sh
   ```

4. Visit http://127.0.0.1:8000

### Manual Setup

1. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   python manage.py makemigrations blog
   python manage.py migrate
   ```

4. Create categories:
   ```bash
   python create_categories.py
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start server:
   ```bash
   python manage.py runserver
   ```

## Production Deployment

### Environment Variables

Copy `.env.production` to `.env` and configure:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False`
- `ALLOWED_HOSTS`: Your domain(s)
- `DATABASE_URL`: PostgreSQL connection string
- `CSRF_TRUSTED_ORIGINS`: Trusted origins for CSRF

### Docker

Build and run with Docker:

```bash
docker build -f Dockerfile.prod -t two-spoons-online .
docker run -p 8000:8000 --env-file .env two-spoons-online
```

### GitHub Actions

The repository includes GitHub Actions workflow for:

- Running tests on pull requests
- Building and pushing Docker images to GitHub Container Registry
- Automated deployment on main branch pushes

## Project Structure

```
├── blog/                   # Blog Django app
├── blog_site/             # Main Django project
│   └── settings/          # Split settings files
├── templates/             # HTML templates
├── static/               # Static files
├── .github/workflows/    # GitHub Actions
├── requirements.txt      # Python dependencies
├── Dockerfile.prod       # Production Dockerfile
└── manage.py            # Django management script
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.