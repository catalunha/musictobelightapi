from rest_framework import serializers

from project.accounts.models.account import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "is_active",
        ]
