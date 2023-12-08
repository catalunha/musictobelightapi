from accounts.models.account_model import AccountModel
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = AccountModel
        fields = ("email",)


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = AccountModel
        fields = ("email",)
