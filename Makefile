PROJECT_NAME = PageObjectPlayWright

.PHONY: help install test allure_test

help:
	@echo MyProject - $(PROJECT_NAME)
	@echo "make help - Print this messages"
	@echo "make install - Install dependencies 'requirements|playwright'"
	@echo "make test - Run tests"
	@echo "make allure_test - Run tests + allure"

install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt
	. venv/bin/activate && playwright install
test:
	pytest

allure_test:
	chmod +x start_tests_allure.sh
	./start_tests_allure.sh

.DEFAULT_GOAL := help
