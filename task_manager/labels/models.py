from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Label(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150,
        unique=True
    )
    created_at = models.DateTimeField(
        verbose_name=_("Creation date"),
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Label")
        verbose_name_plural = _("Labels")