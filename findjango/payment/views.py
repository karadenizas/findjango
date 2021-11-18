from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from payment.models import PurchaseOption, UserWallet, PaymentTransaction
import braintree
from braintree import client_token
from django.conf import settings

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def purchasing_option(request):
    packs = PurchaseOption.objects.all()

    context = {
        'packs':packs,
    }
    return render(request, 'payment/purchasing_option.html', context)

def payment_process(request, id):
    if request.method == "POST":
        pack = PurchaseOption.objects.get(id=id)
        user_wallet = UserWallet.objects.get_or_create(user=request.user) # if not exist user wallet, create an user wallet.
        user_wallet = UserWallet.objects.get(user=request.user) # if exist continue

        # start the process
        nonce = request.POST.get('payment_method_nonce', None)
        result = gateway.transaction.sale({
            'amount': pack.total_price,
            'payment_method_nonce': nonce,
            'options': {'submit_for_settlement': True}
        })
        
        if result.is_success:
            PaymentTransaction.objects.create(wallet=user_wallet, transaction_type='buy', braintree_id=result.transaction.id, amount=pack.token_amount)
            user_wallet.braintree_id = result.transaction.id
            user_wallet.token += pack.token_amount
            user_wallet.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        client_token = gateway.client_token.generate()
        context = {
            'client_token': client_token
        }
        return render(request, 'payment/process.html', context)

def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')