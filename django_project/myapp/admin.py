from django.contrib import admin

from .models import FakeModel


@admin.register(FakeModel)
class FakeModelAdmin(admin.ModelAdmin):
    pass
