from django.db.models import Manager
from django.db.models.query import QuerySet


class CustomManager(Manager):
    def get_not_deleted(self, **extra_fields) -> QuerySet:
        return self.filter(is_delete=False)

    def get_active(self, **extra_fields) -> QuerySet:
        return self.get_not_deleted().filter(is_active=True)
