.PHONY: install collectstatic migrate build render-start

install:
	poetry install

collectstatic:
	poetry run python manage.py collectstatic --no-input

migrate:
	poetry run python manage.py migrate

build:
	./build.sh

render-start:
	poetry run gunicorn task_manager.wsgi