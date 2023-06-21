.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

# -----------------------------------------------------------------------------

python_version=3.9.11
venv=djangoextensionstoo_env

# -----------------------------------------------------------------------------
# Environment setup
# -----------------------------------------------------------------------------

env:  ## create virtualenv
		pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

reqs:  ## install development requirements
		python -m pip install -U pip \
				&& python -m pip install -r requirements.txt \
				&& python -m pip install -r requirements_dev.txt \
				&& python -m pip install -r requirements_test.txt

destroy_env:  ## destroy pyenv virtualenv
		pyenv uninstall ${venv}

# -----------------------------------------------------------------------------
# Django
# -----------------------------------------------------------------------------

python manage.py makemigrations:  ## create django migrations
		python manage.py makemigrations

migrate:  ## apply django migrations
		python manage.py migrate

createsuperuser:  ## create django superuser
		python manage.py createsuperuser

collectstatic:  ## django collect static
		python manage.py collectstatic

serve:  ## serve django development app
		python manage.py runserver 0.0.0.0:8080

scratch: env reqs migrate createsuperuser serve


# Quick tests
delete_unreferenced_files:
		python manage.py delete_unreferenced_files --dry-run

get_all_permissions:
		python manage.py get_all_permissions

manifest_storage_check:
		python manage.py manifest_storage_check

missing_files:
		python manage.py missing_files

fix_proxy_permissions:
		python manage.py fix_proxy_permissions

# -----------------------------------------------------------------------------
# Cleanup
# -----------------------------------------------------------------------------

clean: clean-build clean-pyc ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
		rm -fr build/
		rm -fr dist/
		rm -fr .eggs/
		find . -name '*.egg-info' -exec rm -fr {} +
		find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
		find . -name '*.pyc' -exec rm -f {} +
		find . -name '*.pyo' -exec rm -f {} +
		find . -name '*~' -exec rm -f {} +
		find . -name '__pycache__' -exec rm -fr {} +

# -----------------------------------------------------------------------------
# Deploy
# -----------------------------------------------------------------------------

dist: clean ## builds source and wheel package
		python -m build --wheel

release_test: ## upload package to pypi test
		twine upload dist/* -r pypitest

release: dist ## package and upload a release
		twine upload dist/*
