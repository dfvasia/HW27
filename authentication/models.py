from django.contrib.auth.models import AbstractUser
from django.db import models


class LocationUser(models.Model):
    name = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Местоположения пользователя"
        verbose_name_plural = "Местоположения пользователей"


class User(AbstractUser):
    age = models.PositiveSmallIntegerField()
    location = models.ForeignKey(LocationUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def local_name(self):
        return self.location.name if self.location else None



