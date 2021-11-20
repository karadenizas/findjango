from django.shortcuts import render
import requests
from investment.models import CreateInvest
from django.db.models import Count


def index(request, base=None):
    latest_advices = CreateInvest.objects.order_by('-create_time')[:20]
    popular_advices = CreateInvest.objects.annotate(q_count=Count('member')).order_by('-q_count')[:20]

    context = {
        'latest_advices': latest_advices,
        'popular_advices': popular_advices,
    }

    return render(request, 'index.html', context)