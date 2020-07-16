from django.db import models

# Create your models here.
class Employee(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField(max_length=254)
    Phone=models.CharField(max_length=15)
    Address=models.CharField(max_length=200)