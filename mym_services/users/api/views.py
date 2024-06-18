from django.db.models.query import QuerySet
from rest_framework import mixins
from rest_framework.serializers import BaseSerializer

from mym_services.users.api.serializers import CRUDContactSerializer
from mym_services.users.api.serializers import ListCompanySerializer
from mym_services.users.api.serializers import ListContactSerializer
from mym_services.users.models import Company
from mym_services.users.models import Contact
from mym_services.utils.customs_views import AdminBaseViewSet
from mym_services.utils.customs_views import CRUDModelViewSet


class CompanyViewSet(AdminBaseViewSet, mixins.ListModelMixin):
    serializer_class = ListCompanySerializer

    def get_queryset(self) -> QuerySet:
        return Company.objects.get_not_deleted()


class ContactViewSet(AdminBaseViewSet, CRUDModelViewSet, mixins.ListModelMixin):
    def get_queryset(self) -> QuerySet:
        return Contact.objects.get_not_deleted()

    def get_serializer_class(self) -> type[BaseSerializer]:
        serializer_class = CRUDContactSerializer

        if self.action == "list":
            serializer_class = ListContactSerializer
        return serializer_class
