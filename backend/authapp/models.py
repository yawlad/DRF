from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=64, unique=True)
    first_name = models.CharField(_("first name"), max_length=64, blank=True)
    last_name = models.CharField(_("last name"), max_length=64, blank=True)
    email = models.EmailField(_("email"), unique=True)
    age = models.PositiveIntegerField(_("age"), null=True, blank=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    objects = UserManager()
