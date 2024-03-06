# Django Extensions Too

Author:Tim Santor <tsantor@xstudios.com>

## Overview

Django Extensions Too is a collection of custom extensions for the Django Framework. It is recommended as a supplement to the excellent https://github.com/django-extensions/django-extensions

## Quickstart

To install Django Extensions Too:

```bash
python3 -m pip install django-extensions-too
```

### Settings

To enable `django_extensions_too` in your project you need to add it to `INSTALLED_APPS` in your projects `settings.py` file:

```python
INSTALLED_APPS = (
  'django_extensions_too',
)
```

## Using It

Run `python3 manage.py` and view the available `[django_extensions_too]` management_commands.

## Local Development

1. `make env`
1. `make reqs`
1. `make makemigrations`
1. `make migrate`
1. `make superuser`
1. `make serve`

- Visit `http://127.0.0.1:8000/admin/` for the Django Admin
- Visit `http://127.0.0.1:8000/api/docs/` for the API docs

### Testing

Currently django_spaday has **94%** test coverage.

- Pytest: `make pytest`
- Coverage: `make coverage`
  - Open Report: `make open_coverage`

## Issues

If you experience any issues, please create an [issue](https://bitbucket.org/tsantor/django-extensions-too/issues) on Bitbucket.
