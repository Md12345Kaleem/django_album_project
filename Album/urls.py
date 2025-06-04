from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from album_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('add/',views.add,name="add"),
    path('addrec/',views.add,name="addrec"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
