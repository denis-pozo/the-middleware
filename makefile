.PHONY: start run kill admin

start:
	uv pip install -r requirements.txt
	python3 manage.py migrate

run:
	python3 manage.py runserver

kill:
	lsof -ti :8000 | xargs kill -9 2>/dev/null || true

admin:
	python3 manage.py createsuperuser
