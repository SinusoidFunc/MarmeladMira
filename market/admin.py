from django.conf import settings
from django.contrib import admin
from .models import SliderImage


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name" + 'id']}


admin.site.register(SliderImage)
