Django Extensions Too
=====================

Author:Tim Santor tsantor@xstudios.agency

Overview
========

Django Extensions is a collection of custom extensions for the Django
Framework. It is recommended as a supplement to the excellent
https://github.com/django-extensions/django-extensions

Getting It
==========

To install Django Extensions Too, just use pip:

::

    $ pip install django-extensions-too

To install the development version:

::

    $ pip install git+https://bitbucket.org/tsantor/django-extensions-too.git

If you want to install it from source, grab the git repository and run
setup.py:

::

    $ git clone https://bitbucket.org/tsantor/django-extensions-too.git
    $ cd django-extensions-too
    $ python setup.py install

Installing It
=============

To enable django\_extensions\_too in your project you need to add it to
INSTALLED\_APPS in your projects settings.py file:

::

    INSTALLED_APPS = (
        ...
        'django_extensions_too',
        ...
    )

Using It
========

Delete all files from MEDIA\_ROOT which are not referenced in the
database.

::

    $ python manage.py delete_unreferenced_files

Show a list of all files missing from MEDIA\_ROOT that are referenced in
the database.

::

    $ python manage.py missing_files

Completely remove an installed app from a project. Removes all model
related tables as well as all traces from auth\_permissions,
djang\_admin\_log, django\_content\_type, django\_migrations, etc.

::

    $ python manage.py remove_app

Adds permissions where the model actually references the proxy model and
not the original model.

::

    $ python manage.py fix_proxy_permissions

Documentation
=============

You can view documentation online at:

-  TODO

Or you can look at the docs/ directory in the repository.

Issues
======

If you experience any issues, please create an
`issue <https://bitbucket.org/tsantor/django-extensions-too/issues>`__
on Bitbucket.
