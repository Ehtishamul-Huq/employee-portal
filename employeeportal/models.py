from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.TextField(max_length=100)
    designation = models.TextField(max_length=100)
    joining_date = models.DateField()