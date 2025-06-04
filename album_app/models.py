from django.db import models

# Create your models here.
class album_data(models.Model):
  album_image = models.ImageField(upload_to='photo/')