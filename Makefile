SHELL := /bin/bash

startproject:
	django-admin startproject goldenweb ./src

startapp:
	python3 ./src/manage.py startapp main ./src/main
