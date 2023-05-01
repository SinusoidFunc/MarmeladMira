from django.db import models


class SliderImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/slider')
    uploaded = models.DateTimeField(auto_now_add='YYYY-MM-DD HH:MM')
    text = models.TextField()
