from accounts.exceptions import EmailServiceUnavaliable
from accounts.serializers.account_create_serializer import AccountCreateSerializer
from accounts.serializers.account_new_password_serializer import (
    AccountNewPasswordSerializer,
)
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ParseError, Throttled
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.accounts.models.profile import Profile
from project.accounts.models.reset_password_number import ResetPasswordNumber


class AccountViewCreate(APIView):
    def post(self, request):
        print("AccountViewCreate.post")
        print("request.data", request.data)
        # TODO nao deveria ser data=request.data
        accountCreateSerializer = AccountCreateSerializer(request.data)
        accountCreateSerializer.is_valid(raise_exception=True)

        email = accountCreateSerializer.validated_data["email"]
        password = accountCreateSerializer.validated_data["password"]

        user = get_user_model().objects.create_user(email, password)
        user.save()

        self._createProfile(user)

        return Response({"id": user.id})

    def _createProfile(slef, user):
        Profile.objects.create(user=user)


class AccountViewMe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("AccountViewMe.get")
        print("request.data", request.data)

        user = self.request.user

        return Response(
            {
                "id": user.id,
                "email": user.email,
                "is_active": user.is_active,
            }
        )


class AccountViewResetPassword(APIView):
    def post(self, request):
        print("AccountViewResetPassword.post")
        print("request.data", request.data)

        if request.data.get("email") is None:
            raise ParseError("O campo email não foi informado")
        email = request.data.get("email")

        user = get_object_or_404(
            get_user_model().objects.all(),
            email=email,
        )
        print("user.id", user.id)

        number = self._update_number(user.email)

        self._send_mail(user.email, number)

        return Response({"detail": "Enviamos um email com instruções"})

    def _update_number(self, email):
        updated = True
        if not updated:
            raise Throttled(wait=60 * 60)
        ResetPasswordNumber.objects.filter(email=email).delete()
        resetPasswordNumber = ResetPasswordNumber.objects.create(
            email=email,
        )
        return resetPasswordNumber.number

    def _send_mail(self, email, number):
        print(f"Email: {email} Numero: {number}")

        send_mail(
            "MusicToBeLight - Recuperação de senha",
            f"Seu número de recuperação de senha é {number}",
            "heetoo.dev.01@gmail.com",
            [email],
            fail_silently=False,
        )
        sent = True
        if not sent:
            raise EmailServiceUnavaliable()


class AccountViewNewPassword(APIView):
    def post(self, request):
        print("AccountViewNewPassword.post")
        print("request.data", request.data)

        accountNewPasswordSerializer = AccountNewPasswordSerializer(data=request.data)
        accountNewPasswordSerializer.is_valid(raise_exception=True)

        email = accountNewPasswordSerializer.validated_data["email"]
        number = accountNewPasswordSerializer.validated_data["number"]
        password = accountNewPasswordSerializer.validated_data["password"]

        resetPasswordNumber = get_object_or_404(
            ResetPasswordNumber.objects.all(),
            email=email,
            number=number,
        )
        print("resetPasswordNumber", resetPasswordNumber)

        user = get_user_model().objects.get(
            email=email,
        )
        user.set_password(password)
        user.save()

        resetPasswordNumber.delete()

        return Response({"detail": "Senha alterada com sucesso"})
