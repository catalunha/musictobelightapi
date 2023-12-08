from accounts.models.account_model import AccountModel
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = [
            "id",
            "email",
            "is_active",
        ]
