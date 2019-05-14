from django.contrib import admin

# Register your models here.

from .models import Image, ImageCategory

admin.site.register(ImageCategory)

admin.site.register(Image)