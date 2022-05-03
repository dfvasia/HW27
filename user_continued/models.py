from django.contrib.auth.models import User
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


class ContinuedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.PositiveSmallIntegerField()
    location = models.ForeignKey(LocationUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Доп. поля пользователя"
        verbose_name_plural = "Доп. поля пользователей"

    @property
    def local_name(self):
        return self.location.name if self.location else None



