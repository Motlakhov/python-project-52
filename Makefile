.PHONY: install collectstatic migrate

install:
	poetry install

collectstatic:
	python3 manage.py collectstatic --no-input

migrate:
	python3 manage.py migrate

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi