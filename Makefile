# variables
SCRIPTS_PATH := ./scripts
PROJECT_NAME := page-object-playwright

.PHONY: help init tests tests_allure

help:
	@echo MyProject - $(PROJECT_NAME)
	@echo "make help - Print this messages"
	@echo "make init - Install dependencies 'requirements|playwright'"
	@echo "make tests - Run tests"
	@echo "make tests_allure - Run tests + allure server"

init:
	chmod +x ${SCRIPTS_PATH}/check_poetry.sh && \
	sh ${SCRIPTS_PATH}/check_poetry.sh
	cd pop \
	&& poetry install \
	&& poetry run playwright install

tests:
	cd pop && \
	poetry run pytest -s

tests_allure:
	chmod +x ${SCRIPTS_PATH}/start_tests_allure.sh && \
	sh ${SCRIPTS_PATH}/start_tests_allure.sh

.DEFAULT_GOAL := help
