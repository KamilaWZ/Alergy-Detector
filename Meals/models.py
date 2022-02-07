from unicodedata import name
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=False)
    allergy_potential = models.IntegerField(default=1)