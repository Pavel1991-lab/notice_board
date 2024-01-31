from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Менеджер должен быть унаследован от следующего класса
from django.contrib.auth.models import BaseUserManager

from users.manegement import UserManager


# Менеджер должен содержать как минимум две следующие функции


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]


    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin



    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


    objects = UserManager()


