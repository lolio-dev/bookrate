from django.urls import path

from apps.reviews.views import feed

urlpatterns = [
    path("feed", feed, name="feed")
]
