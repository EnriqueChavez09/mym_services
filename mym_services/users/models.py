from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords

from mym_services.utils.customs_models import CustomModel
from mym_services.utils.regexs import phone_validator

from .managers import CompanyManager
from .managers import ContactManager
from .managers import UserManager


class User(AbstractUser, CustomModel):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(verbose_name="Correo", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()


class Company(CustomModel):
    ruc_number = models.CharField(
        verbose_name="Número de RUC",
        max_length=11,
        unique=True,
    )
    company_name = models.CharField(verbose_name="Razón Social", max_length=100)
    address = models.CharField(verbose_name="Dirección", max_length=100)
    district = models.CharField(verbose_name="Distrito", max_length=100)

    history = HistoricalRecords()

    objects: ClassVar[UserManager] = CompanyManager()

    def __str__(self):
        return f"{self.company_name} - {self.ruc_number}"

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["company_name"]


class Contact(CustomModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name="Empresa",
    )

    full_names = models.CharField(verbose_name="Nombres completos", max_length=100)
    phone = models.CharField(
        verbose_name="Celular",
        max_length=9,
        validators=[phone_validator],
    )
    address = models.CharField(verbose_name="Dirección", max_length=100)
    email = models.EmailField(verbose_name="Correo")

    history = HistoricalRecords()

    objects: ClassVar[UserManager] = ContactManager()

    def get_company(self):
        return self.company.company_name

    def __str__(self):
        return f"{self.full_names}"

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["-created"]
