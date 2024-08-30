from django.db import models
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=25, null=False)
    phone = models.CharField(max_length=15, null=True, blank=True)  # Added phone field
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.
