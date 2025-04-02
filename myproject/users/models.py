
from django.db import models

class User(models.Model):
    last_name = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    father_name = models.CharField(max_length=45, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    number = models.CharField(max_length=11, blank=True, null=True)
    number_polis = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=15, default='Пациент')

    def __str__(self):
        return f"{self.name} {self.last_name}"
    

    