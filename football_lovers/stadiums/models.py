from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Stadium(models.Model):
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 5
    COUNTRY_MAX_LENGTH = 25
    COUNTRY_MIN_LENGTH = 3

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
        ),
    )

    country = models.CharField(
        max_length=COUNTRY_MAX_LENGTH,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(COUNTRY_MIN_LENGTH),
        ),
    )

    capacity = models.IntegerField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
