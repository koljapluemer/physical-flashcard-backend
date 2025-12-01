run:
    (cd ../physical-flashcard-manager && npm run dev) &
    (cd ../physical-flashcard-renderer && npm run dev) &
    (cd ../physical-flashcard-backend && uv run python manage.py runserver) &
    wait
