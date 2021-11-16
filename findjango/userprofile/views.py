from django.shortcuts import render
from django.views.generic import CreateView
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

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'userprofile/user_profile.html', context)