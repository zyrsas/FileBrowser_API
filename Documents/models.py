# -*- coding: utf8 -*-
from django.db import models


# BEGIN User!!! =================================
class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    regID = models.CharField(max_length=300, default="")
    access = models.BooleanField(default=False, verbose_name="Разрешить доступ")

    class Meta:
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователя"

    def __str__(self):
        return self.name

# END User!!! =================================

