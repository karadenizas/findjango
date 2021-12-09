from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from investment.models import CreateInvest


def index(request):
    latest_advices = (CreateInvest
                      .objects
                      .filter(active=True)
                      .order_by('-create_time'))
    popular_advices = (CreateInvest
                       .objects
                       .filter(active=True)
                       .annotate(q_count=Count('member'))
                       .order_by('-q_count'))

    context = {
        'latest_advices': latest_advices,
        'popular_advices': popular_advices,
    }
    return render(request, 'index.html', context)


def htmx_latest_advices(request):
    latest_advices = (CreateInvest
                      .objects
                      .filter(active=True)
                      .order_by('-create_time'))

    paginator = Paginator(latest_advices, 8)
    page = request.GET.get('page')
    try:
        paginate_advices = paginator.page(page)
    except PageNotAnInteger:
        paginate_advices = paginator.page(1)
    except EmptyPage:
        paginate_advices = paginator.page(paginator.num_pages)

    context = {
        'latest_advices': latest_advices,
        'paginate_advices': paginate_advices,
    }
    return render(request, 'htmx_latest_advices.html', context)


def htmx_popular_advices(request):
    popular_advices = (CreateInvest
                      .objects
                      .filter(active=True)
                      .annotate(q_count=Count('member'))
                      .order_by('-q_count'))

    paginator = Paginator(popular_advices, 8)
    page = request.GET.get('page')
    try:
        paginate_advices = paginator.page(page)
    except PageNotAnInteger:
        paginate_advices = paginator.page(1)
    except EmptyPage:
        paginate_advices = paginator.page(paginator.num_pages)

    context = {
        'popular_advices': popular_advices,
        'paginate_advices': paginate_advices,
    }
    return render(request, 'htmx_popular_advices.html', context)