from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from football_lovers.accounts.validators import only_alphabetical_letters_validator


class ChoiceMixin:
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Gender(ChoiceMixin, Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class CustomUser(auth_models.AbstractUser):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            only_alphabetical_letters_validator,
        ),
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            only_alphabetical_letters_validator,
        ),
    )

    gender = models.CharField(
        null=True,
        blank=True,
        choices=Gender.choices(),
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
