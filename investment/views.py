import requests

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from investment.forms import CreateInvestForm
from investment.models import CreateInvest
from investment.decorators import member_check
from userprofile.models import Profile
from payment.models import UserWallet


@login_required
def create_form(request):
    currencies_response = requests.get(
        'https://api.frankfurter.app/currencies')
    currencies = currencies_response.json()

    context = {
        'currencies': currencies,
        'form': CreateInvestForm()
    }
    return render(request, 'investment/create_invest.html', context)


def htmx_latest_rate(request):
    base = request.POST.get('rate')
    latest_repsonse = requests.get(
        'https://api.frankfurter.app/latest?from=' + base)
    latest_rate = latest_repsonse.json()

    return render(request,
                  'investment/htmx_latest_rates.html',
                  {'latest_rate': latest_rate})


@login_required
def htmx_create_invest(request):
    form = CreateInvestForm()
    currencies_response = requests.get(
        'https://api.frankfurter.app/currencies')
    currencies = currencies_response.json()

    if request.method == "POST":
        form = CreateInvestForm(request.POST)
        base_currency = request.POST.get('base_currency')
        target_currency = request.POST.get('target_currency')
        payload = {'from': base_currency, 'to': target_currency}
        get_target_url = requests.get(
            'https://api.frankfurter.app/latest', params=payload)
        get_target_json = get_target_url.json()
        get_target_data = get_target_json['rates'][target_currency]

        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.investor = request.user
            user_form.target_value = get_target_data
            user_form.save()
            return HttpResponse("""
                <div class="
                alert alert-secondary bg-transparent 
                text-center text-success fw-bold" 
                role="alert">

                <h4 class="alert-heading fw-bold">
                Advice has been successfully created!
                </h4>

                <p>You can show the your advices from the Profile tab.</p>
                <hr>
                </div>
                """)
            
    context = {
        'form': form,
        'currencies': currencies,
    }
    return render(request, 'investment/htmx_create_invest.html', context)


@login_required
def preview_invest(request, id):
    invest_model = CreateInvest.objects.get(id=id)
    investor_profile = Profile.objects.get(user=invest_model.investor)
    investor_wallet = UserWallet.objects.get(user=invest_model.investor)
    user_wallet = UserWallet.objects.get(user=request.user)

    if (request.user == invest_model.investor 
        or request.user in invest_model.member.all()):
        return redirect('investment:review_invest', id=id)

    if request.method == "POST" and user_wallet.token >= invest_model.token:
        user_wallet.token = user_wallet.token - invest_model.token
        investor_wallet.token += invest_model.token
        invest_model.member.add(request.user)
        user_wallet.save()
        investor_wallet.save()
        return redirect('investment:review_invest', id=id)

    context = {
        'invest_model': invest_model,
        'investor_profile': investor_profile,
    }
    return render(request, 'investment/preview_invest.html', context)


@login_required
@member_check
def review_invest(request, id):
    invest_model = CreateInvest.objects.get(id=id)
    investor_profile = Profile.objects.get(user=invest_model.investor)

    context = {
        'invest_model': invest_model,
        'investor_profile': investor_profile,
    }
    return render(request, 'investment/review_invest.html', context)
