from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from project.accounts.models.account import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email",)


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ("email",)
