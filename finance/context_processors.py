from payment.models import UserWallet
from django.contrib.auth.models import AnonymousUser

def token_view(request):
    if request.user.is_authenticated:
        return {'user_token': UserWallet.objects.get(user=request.user).token}
    return request