from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.reviews.forms import ReviewForm
from utils.books_helper import BooksHelper

book_helper = BooksHelper()


@login_required
def feed(request):
    return render(request, 'reviews/feed.html')


@login_required
def search_books(request):
    if request.method == 'POST':
        query = request.POST['query']

        results = book_helper.get_books(query)

        return render(request, 'reviews/partials/search-results.html', {'books': results})

    return render(request, 'reviews/search-books.html')


@login_required
def write_review(request, book_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        print(request.POST)
        review = form.save(commit=False)
        review.user = request.user
        review.book_id = book_id
        print(review)
        review.save()

        return redirect('index')
    book = book_helper.get_book(book_id)
    form = ReviewForm()
    return render(request, 'reviews/write-review.html', {"book": book, "form": form})
