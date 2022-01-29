import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    """User model."""

    email = models.EmailField(_("email address"), blank=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
