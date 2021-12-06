from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    meal = models.CharField(max_length=200)
    ingredient1 = models.CharField(max_length=200)
    ingredient2 = models.CharField(max_length=200)
    ingredient3 = models.CharField(max_length=200)
    ingredient4 = models.CharField(max_length=200)
    ingredient5 = models.CharField(max_length=200)
    eating_date = models.DateTimeField(default=timezone.now)
    symptoms = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def saving(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.meal 
