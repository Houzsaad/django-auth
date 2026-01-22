from django.db import models

from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    
    def __str__(self):
        return self.name

class Memmber(models.Model):
    name = models.CharField(max_length=20)
    nationality = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class CEO(models.Model):
    name = models.CharField(max_length=45)
    locality = models.TextField()   
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
