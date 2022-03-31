from tkinter import CASCADE
from django.db import models
from django.forms import ChoiceField
import datetime

class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=200, blank=False)
    potential_choices = ((0, 'none'), (1,'low'), (2,'middle'), (3,'high'))
    alergy_potential = models.PositiveSmallIntegerField(blank=False, choices = potential_choices),
    eating_day = models.DateField(blank = False)
    eating_hour = models.TimeField(blank = False)
    relation_with = models.ForeignKey('Meals', on_delete=CASCADE)
    
    
class Meal(models.Model):
    meal_name = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank = True, default=meal_name)


def __str__(self):
        return self.meal_name
   
