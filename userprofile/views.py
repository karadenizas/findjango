from django.shortcuts import redirect, render
from django.views.generic import CreateView
from investment.models import CreateInvest, ResultInvest
from userprofile.forms import UserCreationForm, ProfileChangeForm
from userprofile.models import MyUser, Profile


def my_profile(request):
    pending_advice = CreateInvest.objects.filter(investor=request.user, active=True)
    given_concluded_advice = ResultInvest.objects.filter(investor=request.user)
    purchased_advice = MyUser.objects.get(user_name=request.user).invest.all()
    purchased_concluded_advice = MyUser.objects.get(user_name=request.user).member_result.all()

    context = {
        'pending_advice': pending_advice,
        'given_concluded_advice': given_concluded_advice,
        'purchased_advice': purchased_advice,
        'purchased_concluded_advice': purchased_concluded_advice,
    }
    return render(request, 'userprofile/my_profile.html', context)


class RegisterCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = 'done/'


def register_done(request):
    return render(request, 'registration/register_done.html')


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

def account_settings(request):
    return render(request, 'userprofile/account_settings.html')

def profile_settings(request):
    user_profile = Profile.objects.get(user=request.user)
    form = ProfileChangeForm(instance=user_profile)

    if request.method == "POST":
        form = ProfileChangeForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile:profile_change_done')

    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'userprofile/profile_settings.html', context)

def profile_change_done(request):
    return render(request, 'userprofile/profile_change_done.html')