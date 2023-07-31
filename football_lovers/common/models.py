from django.db import models


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
