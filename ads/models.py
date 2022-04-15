from django.db import models

# Create your models here.
# Id,name,author,price,description,address,is_published


class Advertisement(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    author = models.CharField(max_length=200,null=False, blank=False)
    price = models.PositiveSmallIntegerField(null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    address = models.CharField(max_length=1000, null=False, blank=False)
    is_published = models.BooleanField(default=False)


# id,name
# 1,Котики
# 2,Песики
# 3,Книги
# 4,Растения
# 5,Мебель и интерьер
"""
class Vacancy(models.Model):
    STATUS = [
        ("draft", "Черновик"),
        ("open", "Открыта"),
        ("closed", "Закрыта"),
    ]

    slug = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    status = models.CharField(max_length=6, choices=STATUS, default="draft")
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug
"""

class Characteristics(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
