from allauth.account.decorators import secure_admin_login
from allauth.account.models import EmailAddress
from allauth.mfa.models import Authenticator
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.models import SocialToken
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _
from simple_history.admin import SimpleHistoryAdmin

from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from .models import Company
from .models import Contact
from .models import User

if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://docs.allauth.org/en/latest/common/admin.html#admin
    admin.autodiscover()
    admin.site.login = secure_admin_login(admin.site.login)  # type: ignore[method-assign]

admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(Authenticator)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (
            _("Credenciales"),
            {"fields": ("email", "password")},
        ),
        (
            _("Permisos"),
            {
                "fields": ("is_staff", "is_superuser"),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = ["email", "is_superuser"]
    search_fields = ["email"]
    ordering = ["-pk"]


@admin.register(Company)
class CompanyAdmin(SimpleHistoryAdmin):
    fieldsets = (
        (
            _("Información General"),
            {"fields": ("ruc_number", "company_name", "address", "district")},
        ),
    )
    list_display = [
        "id",
        "ruc_number",
        "company_name",
        "address",
        "district",
        "is_delete",
    ]
    search_fields = ["ruc_number", "company_name"]
    list_display_links = ["id", "ruc_number", "company_name"]


@admin.register(Contact)
class ContactAdmin(SimpleHistoryAdmin):
    fieldsets = (
        (
            _("Información General"),
            {"fields": ("company", "full_names", "phone", "address", "email")},
        ),
    )
    list_display = [
        "id",
        "company",
        "full_names",
        "phone",
        "address",
        "email",
        "is_delete",
    ]
    search_fields = ["full_names", "phone", "email"]
    list_display_links = ["id", "full_names", "company"]
    list_filter = ["company"]
    date_hierarchy = "created"
