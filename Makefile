#
# Makefile for music-library-mvp
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

DEPS ?= $(PWD)/requirements-dev.txt
VENV ?= $(PWD)/venv
MAKE := $(MAKE) --no-print-directory

.PHONY: help venv reset-venv test run docker-up docker-logs clean clean-pyc clean-tests clean-venv
.DEFAULT_GOAL : help

help:
	@echo 'Usage:'
	@echo
	@echo '    make venv            install the package in a virtual environment'
	@echo '    make reset-venv      recreate the virtual environment'
	@echo '    make test            run the test suite, report coverage'
	@echo '    make run             run app/app.py'
	@echo
	@echo '    make docker-up       run docker-compose up'
	@echo '    make docker-down     run docker-compose down'
	@echo '    make docker-logs     run docker-compose logs'
	@echo
	@echo '    make clean           cleanup all temporary files'
	@echo '    make clean-pyc       cleanup python file artifacts'
	@echo '    make clean-tests     cleanup python test artifacts'
	@echo '    make clean-venv      cleanup all virtualenv'
	@echo

venv:
	virtualenv $(VENV) --no-site-packages
	. $(VENV)/bin/activate && \
	pip install -r $(DEPS)

reset-venv:
	$(MAKE) clean
	rm -rf "$(VENV)"
	$(MAKE) venv

test:
	. $(VENV)/bin/activate && \
	py.test -vvra tests

run:
	. $(VENV)/bin/activate && \
	python app.py

docker-up:
	docker-compose up --force-recreate -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

clean:  clean-pyc clean-tests clean-venv

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +

clean-tests:
	find . -name '.cache' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.eggs' -exec rm -fr {} +
	find . -name '*egg-info' -exec rm -fr {} +

clean-venv:
	rm -rf "$(VENV)"
