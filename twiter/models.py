from django.db import models
from django.db.models.signals import post_save
from django.utils.safestring import mark_safe
from decouple import config
# instance of python-twitter
import twitter 
import os

api_client=twitter.Api(
    consumer_key=config('CONSUMER_KEY'),
	consumer_secret=config('CONSUMER_SECRET'),
	access_token_key=config('ACCESS_TOKEN_KEY'),
	access_token_secret=config('ACCESS_TOKEN_SECRET'))
#print(api_client.VerifyCredentials())

#result =   api_client.GetFollowers()
#first_ten= result[:10]
#print(result[0])
#image_path= os.path.abspath('meteorito.jpg')

# Create your models here.
class Twit(models.Model):
    text = models.CharField(max_length=280)
    image = models.ImageField('twits')
    def __str__(self):
        return self.text
    def save(self, *args, **kwargs):
        super(Twit, self).save(*args, **kwargs)
        # send twit with self.text and image overwriting save method 
        api_client.PostUpdate('using save method overwrite: '+ self.text,media=self.image.file.name)
    def thumb_image(self):
        return self.image.url
    def thumbnail(self):
        if self.image:
            return mark_safe(
				f'<image src="{self.image.url}" width=60 height=60 style="border-radius:50%" />'
				)
        else:
            return u'No image file found'
        thumbnail.short_description = 'Picture'
        thumbnail.allow_tags = True


# or send twit with self.text and image using signals
def createTwit(sender, instance, *args, **kwargs):
    api_client.PostUpdate('using model signal post_save: '+instance.text,media=instance.image.file.name)
post_save.connect(createTwit, sender=Twit)



			
			