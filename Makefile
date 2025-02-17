.PHONY: install collectstatic migrate build render-start

install:
	uv pip install . --python=/opt/render/project/src/.render/bin/python3

collectstatic:
	python manage.py collectstatic --noinput

migrate:
	python manage.py migrate

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi