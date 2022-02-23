from unicodedata import name
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=95)
    allergy_potential = models.IntegerField()