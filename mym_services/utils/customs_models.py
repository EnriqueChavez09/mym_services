from django.db import models
from model_utils.models import TimeStampedModel


class CustomModel(TimeStampedModel):
    is_active = models.BooleanField(verbose_name="¿Activo?", default=True)
    is_delete = models.BooleanField(verbose_name="¿Eliminado?", default=False)
    order = models.PositiveIntegerField(verbose_name="Orden", default=1)

    class Meta:
        abstract = True
