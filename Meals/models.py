from unicodedata import name
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    allergy_potential = models.IntegerField(min_value=1, max_value=5)