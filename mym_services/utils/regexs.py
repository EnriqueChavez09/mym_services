from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r"^9\d{8}$",
    message="El número debe empezar con 9 y contener exactamente 9 dígitos.",
)
