from django.db import models

from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=20)
    house_number = models.BinaryField(blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

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

#class Co_founder(models.Model):
    #skills = models.TextField()
    #email = models.EmailField(unique=True)
    ##course = models.ForeignKey(on_delete=models.CASCADE)

    def __str__(self):
        return self.name

