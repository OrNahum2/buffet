from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    imageUrl = models.CharField(max_length=1000)
    isGlutenFree = models.BooleanField(null=True)
    isVegeterian = models.BooleanField(null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Orders(models.Model):
    dishes = models.ManyToManyField(Dish,blank=False)
    time = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + '-' + self.time

    
