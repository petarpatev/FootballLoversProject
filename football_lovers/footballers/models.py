from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Footballer(models.Model):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 2
    NATIONALITY_MAX_LENGTH = 30
    NATIONALITY_MIN_LENGTH = 3

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    team = models.CharField(
        null=True,
        blank=True,
    )

    nationality = models.CharField(
        max_length=NATIONALITY_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(NATIONALITY_MIN_LENGTH),
        ),
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
