from datetime import date, timedelta

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def check_old_years(value: date):
    if value >= (date.today() - timedelta(days=(365*9))):
        raise ValidationError(f'{value} Ты еще слишком мал))')


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
    email = models.EmailField(blank=False, null=False, unique=True)
    age = models.PositiveSmallIntegerField(null=True, validators=[MinValueValidator(9)])
    birth_date = models.DateField(null=False, blank=False, validators=[check_old_years])
    location = models.ForeignKey(LocationUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    # @property
    # def local_name(self):
    #     return self.location.name if self.location else None



