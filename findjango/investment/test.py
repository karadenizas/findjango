import requests
from datetime import date, timedelta
from investment.models import CreateInvest

def testfunc():
    base_currencies = ['AUD', 'BGN', 'BRL', 'CAD',
                    'CHF', 'DKK', 'EUR', 'GBP', 'HKD', 'IDR']
    target_currencies = ['ZAR', 'USD', 'TRY', 'THB',
                        'SEK', 'RUB', 'RON', 'PLN', 'NZD', 'JPY']

    for i in range(1, 11):
        payload = {'from': base_currencies[i-1], 'to': target_currencies[i-1]}
        latest_url = requests.get(
            'https://api.frankfurter.app/latest', params=payload)
        latest_data = latest_url.json()

        CreateInvest.objects.create(
            investor_id=i,
            target_value=latest_data['rates'][target_currencies[i-1]],
            base_currency=base_currencies[i-1],
            target_currency=target_currencies[i-1],
            target_date=date.today() + timedelta(days=1),
            description="This is a bot's description",
            analysis="This is a bot's analysis",
            token=i,
        )
