from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = (
            "email",
            "password",
        )


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = (
            "email",
            "password",
        )
