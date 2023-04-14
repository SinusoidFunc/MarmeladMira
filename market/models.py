from django.db import models


# Create your models here


class Slider(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(null=True, upload_to='photos/%Y/%m/%d/')
    uploaded = models.DateTimeField('date published', blank=True)
