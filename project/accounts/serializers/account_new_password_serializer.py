from rest_framework import serializers


class AccountNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    number = serializers.CharField(max_length=6, min_length=6, required=True)
    password = serializers.CharField(
        required=True,
        min_length=6,
    )

    def validate(self, data):
        if data["email"] == data["password"]:
            raise serializers.ValidationError("Email e Password não pode ser iguais.")
        return data
