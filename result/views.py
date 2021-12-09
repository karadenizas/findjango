from django.shortcuts import render

from investment.models import ResultInvest


def result_index(request):
    invest_result = ResultInvest.objects.all()
    top_earner = ResultInvest.objects.order_by('-total_value')

    context = {
        'invest_result': invest_result,
        'top_earner': top_earner,
    }
    return render(request, 'result/result_index.html', context)


def result_detail(request, id):
    invest_result = ResultInvest.objects.get(id=id)

    context = {
        'invest_result': invest_result,
    }
    return render(request, 'result/result_detail.html', context)