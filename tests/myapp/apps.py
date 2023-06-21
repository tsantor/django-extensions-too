from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "tests.myapp"

    def ready(self):
        pass
