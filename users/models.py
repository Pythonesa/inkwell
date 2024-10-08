from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    phone_number = models.CharField(_("número de teléfono"), max_length=15)

    email = models.EmailField(_("email address"), null=True, blank=True)
    birth_date = models.DateField(_("fecha de nacimiento"), null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
