from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.contrib.auth.models import User
from django.db import models


# this is my customized User Model
from django.urls import reverse
from django.utils import timezone
from django.http import FileResponse


class UserManager(BaseUserManager):

    def create_user(self, phone, username, display_name, password):
        if not phone:
            raise ValueError("Users must have Phone number")
        if not display_name:
            display_name = username

        user = self.model(
            phone = phone,
            username=username,
            display_name=display_name
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, username, display_name, password):
        user = self.create_user(
            phone,
            username,
            display_name,
            password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(unique=True, max_length=len('09123456789'))
    username = models.CharField(max_length=40, unique=True)
    display_name = models.CharField(max_length=140)
    bio = models.CharField(max_length=140, blank=True, default="")
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ["display_name", "username"]

    def __str__(self):
        return '@{}'.format(self.username)

    def get_short_name(self):
        return self.display_name

    def get_long_name(self):
        return "{} (@{})".format(self.display_name, self.username)

    def get_absolute_url(self):
        return reverse('accounts:profile', args=[self.username])
