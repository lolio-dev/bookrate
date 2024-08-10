from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from utils.books_helper import BooksHelper

book_helper = BooksHelper()


@login_required
def feed(request):
    return render(request, 'reviews/feed.html')


@login_required
def search_books(request):
    if request.method == 'POST':
        query = request.POST['query']

        results = book_helper.query(query)

        return render(request, 'reviews/partials/search-results.html', {'books': results})

    return render(request, 'reviews/search-books.html')


@login_required
def write_review(request, book_id):
    print(book_id)
    return render(request, 'reviews/write-review.html', {"book_id": book_id})
