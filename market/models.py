from django.db import models


# TODO: Make product model

class SliderImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/slider')
    # TODO: Remove time zone / check is 'auto_now_add' correct or not
    uploaded = models.DateTimeField(auto_now_add='YYYY-MM-DD HH:MM')
    text = models.TextField()  # the  text to show on slide


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/categories')
    # TODO: understand why 'default' is necessary


class Unit(models.Model):
    name = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    help = models.CharField(max_length=255)



class Position(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/products')
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    unit = models.ForeignKey(to=Unit, on_delete=models.DO_NOTHING)
    ordered_num = models.PositiveIntegerField(
        default=0)  # TODO: Remove ordered_num from admin panel and make it ++ when product is ordered
    slug = models.SlugField()  # TODO: Make Auto Slug Complete or smth like that
    created = models.DateTimeField(auto_now_add="True")
