from rest_framework import serializers

from mym_services.users.models import Company
from mym_services.users.models import Contact


class CRUDContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "full_names", "phone", "address", "email", "company"]


class ListContactSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source="get_company")

    class Meta:
        model = Contact
        fields = ["id", "full_names", "phone", "address", "email", "company", "created"]


class ListCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "company_name"]
