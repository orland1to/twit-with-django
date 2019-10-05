from django.db import models

# Create your models here.
class Twit(models.Model):
    text = models.CharField(max_length=280)
    image = models.ImageField()