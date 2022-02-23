from unicodedata import name
from django.db import models
import datetime

class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=False)
    allergy_potential = models.IntegerField(default=1, blank = False)
    date_pub = models.DateTimeField(blank = False)

    def __str__(self):
        return self.title

