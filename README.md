# Django Extensions Too

![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)

<!-- ![Code Style](https://img.shields.io/badge/code_style-ruff-black) -->

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

Delete all files from `MEDIA_ROOT` (local or cloud) which are not referenced in the database.

```bash
$ python manage.py delete_unreferenced_files
```

Show a list of all files missing from `MEDIA_ROOT`(local or cloud) that are referenced in the database.

```bash
$ python manage.py missing_files
```

Completely remove an installed app from a project. Removes all model related tables as well as all traces from `auth_permissions`, `django_admin_log`, `django_content_type`, `django_migrations`, etc.

```bash
$ python manage.py remove_app appname
```

Adds permissions for proxy models to provide more granular permission control.

```bash
$ python manage.py add_proxy_permissions
```

Output all permission strings:

```bash
$ python manage.py get_all_permissions
```

## Local Development

```bash
make env
make pip_install
make migrations
make migrate
make superuser
make serve
```

or simply `make from_scratch`

- Visit `http://127.0.0.1:8000/admin/` for the Django Admin

### Testing

```bash
make pytest
make coverage
make open_coverage
```

## Issues

If you experience any issues, please create an [issue](https://github.com/tsantor/django-extensions-too/issues) on Github.
