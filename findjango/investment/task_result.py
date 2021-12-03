import requests
from datetime import date
from investment.models import CreateInvest, ResultInvest


# CreateInvest model target date check. If target date is now, set the result value and convert the 'active' true to false.
def target_date_job():
    invests = CreateInvest.objects.filter(target_date=date.today(), active=True)
    for invest in invests:
        payload = {'from':invest.base_currency, 'to':invest.target_currency}
        latest_url = requests.get('https://api.frankfurter.app/latest', params=payload)
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

