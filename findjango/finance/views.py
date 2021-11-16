from django.shortcuts import render
import requests
from django.http import HttpResponse
from investment.models import CreateInvest


def index(request, base=None):
    latest_advices = CreateInvest.objects.order_by('-create_time')[:20]

    context = {
        'latest_advices': latest_advices,
    }

    return render(request, 'index.html', context)
