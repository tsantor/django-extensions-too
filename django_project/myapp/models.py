from django.db import models


class FakeModel(models.Model):

    file = models.FileField(blank=True, null=True)
