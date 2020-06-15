from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('afterglow.urls')),
    path('control/', admin.site.urls),
]
