from enum import IntFlag
from pyexpat import model
from django.db import models
from django.forms import CharField, IntegerField


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.FloatField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
# Create your models here.
