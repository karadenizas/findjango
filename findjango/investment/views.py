from django.shortcuts import redirect, render
from investment.forms import CreateInvestForm
import requests
from investment.models import CreateInvest
from userprofile.models import Profile
from payment.models import UserWallet


def create_form(request):
    form = CreateInvestForm()

    currencies_response = requests.get('https://api.frankfurter.app/currencies')
    currencies = currencies_response.json()

    latest_response = requests.get('https://api.frankfurter.app/latest')
    latest = latest_response.json()

    if request.method == "POST" and request.POST.get('rate'):
        base = request.POST.get('rate')
        latest_response = requests.get('https://api.frankfurter.app/latest?from=' + base)
        latest = latest_response.json()
    

    elif request.method == "POST":
        # take the target value
        base_currency = request.POST.get('base_currency')
        target_currency = request.POST.get('target_currency')
        payload = {'from': base_currency, 'to': target_currency}
        get_target_url = requests.get('https://api.frankfurter.app/latest', params=payload)
        get_target_json = get_target_url.json()
        get_target_data = get_target_json['rates'][target_currency]

        form = CreateInvestForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.investor = request.user
            user_form.target_value = get_target_data
            user_form.save()
            return redirect('profile:my_profile')
        else:
            form = CreateInvestForm()
    

    context = {
        'form': form,
        'currencies': currencies,
        'latest': latest,
    }
    return render(request, 'investment/create_invest.html', context)


def detail_invest(request, id):
    invest_model = CreateInvest.objects.get(id=id)
    investor_profile = Profile.objects.get(user=invest_model.investor)
    investor_wallet = UserWallet.objects.get(user=invest_model.investor)
    user_wallet = UserWallet.objects.get(user=request.user)

    if request.method == "POST" and user_wallet.token >= invest_model.token:
        user_wallet.token = user_wallet.token - invest_model.token
        investor_wallet.token += invest_model.token
        invest_model.member.add(request.user)
        user_wallet.save()
        investor_wallet.save()
        return redirect('index')

    context = {
        'invest_model': invest_model,
        'investor_profile': investor_profile,
    }
    return render(request, 'investment/detail_invest.html', context)