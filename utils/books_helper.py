import json

import requests


class BooksHelper:
    url = "https://www.googleapis.com/books/v1"

    @staticmethod
    def format_book(book):
        volume_info = book.get('volumeInfo')

        return {
            'title': volume_info.get('title'),
            'author': volume_info.get('authors')[0] if volume_info.get('authors') else None,
            'publisher': volume_info.get('publisher'),
            'id': book.get('id'),
            'thumbnail': volume_info.get('imageLinks').get('thumbnail') if volume_info.get('imageLinks') else None,
            'description': volume_info.get('description'),
        }

    def get_books(self, q):
        req = requests.get(f'{self.url}/volumes?q={q}')

        if req.status_code == 200:
            data = req.json()
            return [self.format_book(book) for book in data.get('items')]
        return []

    def get_book(self, q):
        req = requests.get(f'{self.url}/volumes/{q}')
        return self.format_book(req.json())
