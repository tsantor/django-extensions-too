from django.db import models


class TestModel(models.Model):

    file = models.FileField(blank=True, null=True)

