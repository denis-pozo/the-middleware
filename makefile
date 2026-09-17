.PHONY: start kill admin

start:
	uv pip install -r requirements.txt
	python manage.py migrate
	python manage.py runserver

kill:
	lsof -ti :8000 | xargs kill -9 2>/dev/null || true

admin:
	python manage.py createsuperuser
