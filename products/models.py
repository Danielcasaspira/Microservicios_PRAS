from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=8000000)
    date = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass