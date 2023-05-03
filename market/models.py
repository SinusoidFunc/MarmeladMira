from django.db import models


# TODO: Make product model

class SliderImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/slider')
    uploaded = models.DateTimeField(auto_now_add='YYYY-MM-DD HH:MM')
    text = models.TextField()


class Category(models.Model):
    pass


class Unit(models.Model):
    pass


class Position(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/products')
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    unit = models.ForeignKey(to='Unit', on_delete=models.DO_NOTHING)
    ordered_num = models.PositiveIntegerField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add="True")

