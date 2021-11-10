from django.shortcuts import render
import requests
from django.http import HttpResponse


def index(request, base=None):

    # automatic request function
    def requester(url):
        response = requests.get(url)
        response_json = response.json()
        return response_json

    currencies = requester('https://api.frankfurter.app/currencies')
    latest = requester('https://api.frankfurter.app/latest')

    if request.method == "POST":
        base = request.POST.get('rate')
        latest = requester('https://api.frankfurter.app/latest?from=' + base)

    context = {
        'currencies': currencies,
        'latest': latest,
    }

    return render(request, 'index.html', context)
