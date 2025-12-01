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

config/            # Django project settings
```

## Tech stack

- Django 5.2
- Django REST Framework
- PostgreSQL (SQLite for dev)
- Token authentication

## Run locally

### Setup 

- Requires `uv` (install with `pip install uv` if needed).
- copypaste `.env.example` to `.env`

```bash
git submodule add git@github.com:koljapluemer/physical-flashcard-doc.git doc 
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

