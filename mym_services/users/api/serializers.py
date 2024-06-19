from typing import Any

from rest_framework import serializers

from mym_services.users.models import Company
from mym_services.users.models import Contact


class CRUDContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "full_names", "phone", "address", "email", "company"]

    def validate_email(self, value: Any):
        check_if_there_is_any_record = (
            Contact.objects.check_if_there_is_any_record_according_to_email(value)
        )
        if check_if_there_is_any_record:
            raise serializers.ValidationError(["Existe un contacto con ese correo"])
        return value

    def validate_phone(self, value: Any):
        check_if_there_is_any_record = (
            Contact.objects.check_if_there_is_any_record_according_to_phone(value)
        )
        if check_if_there_is_any_record:
            raise serializers.ValidationError(["Existe un contacto con ese celular"])
        return value


class ListContactSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source="get_company")

    class Meta:
        model = Contact
        fields = ["id", "full_names", "phone", "address", "email", "company", "created"]


class ListCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "company_name"]
