from django.shortcuts import render
from django.views.generic import CreateView
from investment.models import CreateInvest, ResultInvest
from userprofile.forms import UserCreationForm
from userprofile.models import Profile


def my_profile(request):
    return render(request, 'userprofile/my_profile.html')


class RegisterCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/'


def user_profile(request, slug):
    user_profile = Profile.objects.get(slug=slug)
    pending_advice = CreateInvest.objects.filter(investor=user_profile.user.id, active=True)
    concluded_advice = ResultInvest.objects.filter(investor=user_profile.user.id)
    
    context = {
        'user_profile': user_profile,
        'pending_advice': pending_advice,
        'concluded_advice': concluded_advice,
    }
    return render(request, 'userprofile/user_profile.html', context)

def profile_settings(request):
    return render(request, 'userprofile/profile_settings.html')