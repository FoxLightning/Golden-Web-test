SHELL := /bin/bash

# startproject:
# 	django-admin startproject goldenweb ./src

# startapp:
# 	python3 ./src/manage.py startapp main ./src/main


ir:
	pip install -r requirements.txt

fr: 
	pip freeze > requirements

ur: ir fr

rs:
	python3 ./src/manage.py runserver

mm:
	python3 ./src/manage.py makemigrations

m:
	python3 ./src/manage.py migrate

mmm: mm m

csu:
	python3 ./src/manage.py createsuperuser

sp:
	python3 ./src/manage.py shell_plus --print-sql

fdb:
	python3 ./src/manage.py fill_db
