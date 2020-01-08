from django.db import models
from django.utils import timezone

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    std = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)