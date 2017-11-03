from django.contrib import admin

# Register your models here.

from .models import HeroInfo, SkinInfo

admin.site.register(HeroInfo)
admin.site.register(SkinInfo)