import uuid

from accounts.managers import AccountManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = AccountManager()

    def __str__(self) -> str:
        return self.email
