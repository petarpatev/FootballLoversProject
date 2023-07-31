from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Team(models.Model):
    NAME_MAX_LENGTH = 35
    NAME_MIN_LENGTH = 1
    COUNTRY_MAX_LENGTH = 25
    COUNTRY_MIN_LENGTH = 3

    name = models.CharField(
        null=False,
        blank=False,
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
    )

    country = models.CharField(
        null=False,
        blank=False,
        max_length=COUNTRY_MAX_LENGTH,
        validators=(
            MinLengthValidator(COUNTRY_MIN_LENGTH),
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
