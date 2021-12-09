from datetime import date, timedelta

import requests

from investment.models import CreateInvest, ResultInvest


"""
CreateInvest model target date check.
If target date is now,
set the result value and convert the 'active' true to false.
"""
def target_date_job():
    invests = (CreateInvest
               .objects
               .filter(target_date=date.today(), active=True))
    for invest in invests:
        payload = {'from':invest.base_currency, 'to':invest.target_currency}
        latest_url = requests.get(
            'https://api.frankfurter.app/latest', params=payload)
        latest_data = latest_url.json()

        invest.active = False
        invest.save()
        q = ResultInvest.objects.create(invest_id=invest.id,
                                        investor_id=invest.investor.id,
                                        start_value=invest.target_value,
                                        result_value=latest_data['rates'][invest.target_currency])
        for i in invest.member.all():
            q.member.add(i.id)
            q.save()

    # Auto advice creation and deletion every day.
    base_currencies = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF',
                       'DKK', 'EUR', 'GBP', 'HKD', 'IDR']
    target_currencies = ['ZAR', 'USD', 'TRY', 'THB', 'SEK',
                         'RUB', 'RON', 'PLN', 'NZD', 'JPY']

    for i in range(1, 11):
        payload = {'from':base_currencies[i-1], 'to':target_currencies[i-1]}
        latest_url = requests.get(
            'https://api.frankfurter.app/latest', params=payload)
        latest_data = latest_url.json()

        CreateInvest.objects.create(
            investor_id = i,
            target_value = latest_data['rates'][target_currencies[i-1]],
            base_currency = base_currencies[i-1],
            target_currency = target_currencies[i-1],
            target_date = date.today() + timedelta(days=1),
            description = "This is a bot's description",
            analysis = "This is a bot's analysis",
            token = i,
        )
    
    # delete old advices
    for i in CreateInvest.objects.all()[20:]:
        i.delete()

    # delete old results
    for i in ResultInvest.objects.all()[10:]:
        i.delete()