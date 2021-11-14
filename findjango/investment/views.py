from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView
from investment.forms import CreateInvestForm
import requests
from investment.models import CreateInvest
from django.core.exceptions import ValidationError


# class CreateInvestFormView(FormView):
#     template_name = 'investment/create_invest.html'
#     form_class = CreateInvestForm
#     success_url = '/profile/'

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         form.full_clean()

#         if form.is_valid():            
#             base_currency = self.request.POST.get('base_currency')
#             target_currency = self.request.POST.get('target_currency')

#             payload = {'from': base_currency, 'to': target_currency}
#             target_url = requests.get('https://api.frankfurter.app/latest', params=payload)
#             target_json = target_url.json()
#             target_data = target_json['rates'][target_currency]

#             form.target_value = target_data

#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         form = form.save(commit=False)
#         form.investor = self.request.user
#         form.save()
#         return super().form_valid(form)
      

#     def get_context_data(self, **kwargs):
#         r = requests.get('https://api.frankfurter.app/currencies')
#         currencies = r.json()
#         kwargs['currencies'] = currencies
#         return super().get_context_data(**kwargs)


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
            return redirect('profile:profile')
        else:
            form = CreateInvestForm()
    

    context = {
        'form': form,
        'currencies': currencies,
        'latest': latest,
    }
    return render(request, 'investment/create_invest.html', context)