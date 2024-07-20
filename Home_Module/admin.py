from django.contrib import admin

from Home_Module.models import *


@admin.register(SiteSettingModel)
class SiteSettingAdmin(admin.ModelAdmin):
    ...


@admin.register(SiteBannerModel)
class SiteBannerAdmin(admin.ModelAdmin):
    ...
