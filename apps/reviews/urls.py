from django.urls import path

from apps.reviews.views import feed, search_books, write_review

urlpatterns = [
    path("feed/", feed, name="feed"),
    path("search-books/", search_books, name="search_books"),
    path("reviews/create/<str:book_id>/", write_review, name="write_review"),
]
