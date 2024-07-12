from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path("", index, name="index"),
    path("", include('apps.social.urls')),
    path("admin/", admin.site.urls),
]
