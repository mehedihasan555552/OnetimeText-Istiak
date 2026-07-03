# One-Time Text Django Project

A full Django website where each visitor gets one unique text from the database, and that text is deleted permanently right after retrieval.

## Access rules

- Only the Django admin can add text records.
- Normal visitors cannot access any public add-text page.
- Remaining record count is visible only to authenticated admin users.
- Admin-only operational notes are hidden from normal visitors.

## Features

- Beautiful responsive visitor page.
- Mobile-friendly design.
- Django admin support for managing texts.
- SQLite for local development.
- PostgreSQL-ready settings for real concurrent production traffic.
- Concurrency-safe retrieval pattern with `select_for_update(skip_locked=True)` when the database supports it.

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Add data

Use Django admin only:

- Open `/admin/`
- Log in as superuser/admin
- Add records under `One-time texts`

## URLs

- `/` visitor page
- `/admin/` admin login and text management

## Best production choice

For your exact requirement, PostgreSQL is strongly recommended in production. That is the safest option when multiple users visit at the same time and each must receive a different text.
