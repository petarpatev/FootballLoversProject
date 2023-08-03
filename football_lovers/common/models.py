from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Story(models.Model):
    TITLE_MAX_LENGTH = 40

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False,
    )
    content = models.TextField(
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_story = models.ForeignKey(
        Story, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
