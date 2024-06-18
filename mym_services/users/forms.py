from typing import TYPE_CHECKING

from allauth.account.models import EmailAddress
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

if TYPE_CHECKING:
    from .models import User


class CustomUserChangeForm(UserChangeForm):
    def save(self, commit):
        user: User = super().save(commit=False)
        self.save_m2m()
        last_email: EmailAddress = EmailAddress.objects.filter(user=user).last()
        if last_email:
            last_email.email = user.email
            last_email.save()
        return user


class CustomUserCreationForm(UserCreationForm):
    def save(self, commit):
        user: User = super().save(commit=True)
        EmailAddress.objects.create(
            user=user,
            email=user.email,
            verified=True,
            primary=True,
        )
        return user
