from payment.models import UserWallet


def token_view(request):
    if request.user.is_authenticated:
        return {'user_token': UserWallet
                              .objects
                              .get(user=request.user)
                              .token}
    return request