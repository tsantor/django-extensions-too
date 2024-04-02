from django.db import models


class FakeModel(models.Model):
    file = models.FileField(blank=True, null=True)

    # class Meta:
    #     app_label = "test app"

    def __str__(self):
        return "Fake Model"


class FakeProxyModel(FakeModel):
    class Meta:
        proxy = True
