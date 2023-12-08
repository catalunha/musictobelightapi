import random

from bases.models import BaseModel
from django.db import models


def create_number():
    number = "".join(random.choice("1234567890") for _ in range(6))
    return number


class ResetPasswordNumber(BaseModel):
    email = models.EmailField()
    number = models.CharField(
        max_length=6,
        default=create_number,
        blank=True,
    )

    def __str__(self) -> str:
        return f"id:{self.id}, email:{self.email}, number:{self.number}"
