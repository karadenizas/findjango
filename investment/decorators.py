from django.shortcuts import redirect

from investment.models import CreateInvest


def member_check(function):
    def wrapper(request, id, *args, **kwargs):
        model = CreateInvest.objects.get(id=id)
        if (request.user in model.member.all()
            or request.user == model.investor):
            return function(request, id, *args, **kwargs)
        else:
            return redirect('investment:preview_invest', id=id)
    return wrapper