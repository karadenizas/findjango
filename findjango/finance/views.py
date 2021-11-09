from django.shortcuts import render
import requests
from django.http import HttpResponse

def index(request):
    payload = {'q': 'harry potter'}
    dataview = requests.get('https://openlibrary.org/search.json', params=payload)
    json_data = dataview.json()
    books = json_data.get('docs')

    for book in books:
        name = book.get('title')
        publisher = book.get('publisher')
        language = book.get('language')

        context = {
            'name': name,
            'publisher': publisher,
            'language': language,
        }
        return render(request, 'index.html', context)