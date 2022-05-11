
from django.db import models

from authentication.models import User


class Characteristics(models.Model):
    slug = models.SlugField(max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"
        ordering = ['pk']


class Advertisement(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    price = models.PositiveSmallIntegerField(null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Characteristics, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "объявление"
        verbose_name_plural = "объявления"
        ordering = ['pk']

    @property
    def username(self):
        return self.author.username if self.author else None

