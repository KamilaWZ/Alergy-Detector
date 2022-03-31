from django.db import models
from django.forms import ChoiceField
import datetime

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=200, blank=False)
    potential_choices = ((0,0), (1,1), (2,2), (3,3))
    alergy_potential = models.PositiveSmallIntegerField(blank=False, choices = potential_choices),
    eating_date = models.DateTimeField(blank = False)

    def __str__(self):
            return self.ingredient
