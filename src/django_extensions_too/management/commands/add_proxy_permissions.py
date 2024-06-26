from django.apps import apps
from django.contrib.auth.management import _get_all_permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from django_extensions_too.management.color import color_style

# -----------------------------------------------------------------------------


class Command(BaseCommand):
    help = "Add permissions for proxy models."

    def handle(self, *args, **options):
        self.style = color_style()

        for model in apps.get_models():
            opts = model._meta  # noqa: SLF001
            ctype, created = ContentType.objects.get_or_create(
                app_label=opts.app_label,
                model=opts.object_name.lower(),
            )

            for codename, name in _get_all_permissions(opts):
                p, created = Permission.objects.get_or_create(
                    codename=codename, content_type=ctype, defaults={"name": name}
                )
                if created:
                    self.stdout.write(f"Adding permission {p}")
