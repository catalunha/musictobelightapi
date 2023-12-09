from accounts.forms import AccountChangeForm, AccountCreationForm
from accounts.models.account_model import AccountModel
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    model = AccountModel
    add_form = AccountCreationForm
    form = AccountChangeForm
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fields = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        None,
        {
            "classes": ("wide"),
            "fields": (
                "email",
                "password1",
                "password2",
                "is_staff",
                "is_active",
                "groups",
                "user_permissions",
            ),
        },
    )
