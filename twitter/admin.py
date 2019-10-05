from django.contrib import admin
from .models import Twit
# Register your models here.
admin.site.register(Twit)
def __str__(self):
    return self.text
def thubm_image(self):
    return self.image