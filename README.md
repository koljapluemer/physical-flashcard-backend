# Flashcard Manager

Internal flashcard management REST API for author team.

## What it does

- Create/edit flashcards via REST API
- Organize flashcards into collections
- Token-based authentication (email + password)

## Structure

```
flashcards/                    # Single consolidated app
├── models/
│   ├── user.py               # User model (email-based auth)
│   └── flashcard.py          # Flashcard + FlashcardCollection
├── serializers/
│   ├── auth.py               # Email auth token serializer
│   └── flashcard.py          # Flashcard serializers
├── views/
│   ├── auth.py               # Token authentication view
│   └── flashcard.py          # Flashcard API viewsets
├── admin.py                  # Admin for User + Flashcards
└── migrations/

flashcard_manager/            # Django project settings
```

## Tech stack

- Django 5.2
- Django REST Framework
- PostgreSQL (SQLite for dev)
- Token authentication

## API

See [API.md](API.md) for complete API documentation.

### Quick start

```
POST /api/token-auth/          # Get auth token (email + password)
GET  /api/collections/         # List collections
POST /api/collections/         # Create collection
GET  /api/flashcards/          # List flashcards
POST /api/flashcards/          # Create flashcard
```

## Run locally


### Setup 

- Requires `uv` (install with `pip install uv` if needed).
- copypaste `.env.example` to `.env`

```bash
uv sync --no-dev
uv run python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=admin \
uv run python manage.py createsuperuser \
  --noinput \
  --email admin@example.com
```

### Daily 

```bash
uv run python manage.py runserver
```

...or, to run all

```bash
just run
```

## Authentication

Obtain a token:
```bash
curl -X POST http://localhost:8000/api/token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
```

Use the token in subsequent requests:
```bash
curl http://localhost:8000/api/collections/ \
  -H "Authorization: Token your-token-here"
```
