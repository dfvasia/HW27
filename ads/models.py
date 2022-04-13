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