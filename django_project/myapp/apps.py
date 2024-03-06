from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "django_project.myapp"

    def ready(self):
        pass
