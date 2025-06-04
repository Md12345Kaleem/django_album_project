from django.contrib import admin
from .models import album_data
# Register your models here.

@admin.register(album_data)
class album_data_admim(admin.ModelAdmin):
  list_display = ['id','album_image']
