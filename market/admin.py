from django.conf import settings
from django.contrib import admin
from .models import SliderImage, Position, Unit, Category


# TODO: auto-complete of slug
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


admin.site.register(SliderImage)
admin.site.register(Position)
admin.site.register(Unit)
admin.site.register(Category)
# admin.site.register(ProductAdmin)
