# Django Extensions Too
Author: Tim Santor <tsantor@xstudios.agency>

# Using It
Delete all files from `MEDIA_ROOT` which are not referenced in the database.

    $ python manage.py delete_unreferenced_files


Show a list of all files missing from `MEDIA_ROOT` that are referenced in the database.

    $ python manage.py missing_files


Completely remove an installed app from a project. Removes all model related tables as well as all traces from `auth_permissions`, `django_admin_log`, `django_content_type`, `django_migrations`, etc.

    $ python manage.py remove_app appname


Adds permissions where the model actually references the proxy model and not the original model.

    $ python manage.py fix_proxy_permissions
