from django.db import models

from ads.models import Advertisement
from authentication.models import User


class Selection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=150)
    ad = models.ManyToManyField(Advertisement)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Выборка"
        verbose_name_plural = "Выборки"
        ordering = ['pk']

    def __str__(self):
        return self.name
