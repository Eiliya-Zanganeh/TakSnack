from django.contrib import admin

from Food_Module.models import *


@admin.register(SandwichModel)
class SandwichAdmin(admin.ModelAdmin):
    list_display = ['name', 'offer', 'price', 'offer_price', 'is_special', 'is_active']
    list_filter = ['is_special', 'is_active']
    list_editable = ['is_active']


@admin.register(DrinkModel)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'offer', 'price', 'offer_price', 'is_active']
    list_filter = ['is_active']
    list_editable = ['is_active']


# @admin.register(SauceModel)
# class SauceAdmin(admin.ModelAdmin):
#     ...
