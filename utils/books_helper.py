import json

import requests


class BooksHelper:
    url = "https://www.googleapis.com/books/v1"

    def query(self, q):
        req = requests.get(f'{self.url}/volumes?q={q}')

        if req.status_code == 200:
            data = req.json()
            results = []
            for book in data.get('items'):
                volume_info = book.get('volumeInfo')
                results.append({
                    'title': volume_info.get('title'),
                    'author': volume_info.get('authors')[0] if volume_info.get('authors') else None,
                    'publisher': volume_info.get('publisher'),
                    'id': book.get('id'),
                    'thumbnail': volume_info.get('imageLinks').get('thumbnail') if volume_info.get('imageLinks') else None,
                })
            return results
