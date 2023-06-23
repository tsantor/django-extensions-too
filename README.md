# Django Extensions Too
Author:Tim Santor <tsantor@xstudios.com>

## Overview
Django Extensions Too is a collection of custom extensions for the Django Framework. It is recommended as a supplement to the excellent https://github.com/django-extensions/django-extensions


## Getting It
To install Django Extensions Too, just use pip:

```bash
$ pip install django-extensions-too
```


## Installing It
To enable `django_extensions_too` in your project you need to add it to `INSTALLED_APPS` in your projects `settings.py` file:

```python
INSTALLED_APPS = (
  'django_extensions_too',
)
```

## Using It
Run `python manage.py` and view the available `[django_extensions_too]` management_commands.

## Development

    make env
    make reqs
    pip install -e .

## Testing
Project is at **76%** test coverage.

    python3 runtests.py

    pytest -v
    tox

    # Run coverage
    pytest --cov-report html --cov-report term --cov=tests/


## Issues
If you experience any issues, please create an [issue](https://bitbucket.org/tsantor/django-extensions-too/issues) on Bitbucket.
