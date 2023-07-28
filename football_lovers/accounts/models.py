from django.db import models
from django.contrib.auth import models as auth_models


class CustomUser(auth_models.AbstractUser):
    pass
