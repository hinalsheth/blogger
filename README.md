# Blogger

Webapp to allow creating blog posts implemented in Django

## Usage

```bash
poetry install

poetry run python manage.py migrate

# Create login with admin / admin for a test user
poetry run python manage.py createsuperuser

# Run app locally
poetry run python manage.py runserver

poetry run playwright install

# Run e2e playwright tests
poetry run pytest
```
