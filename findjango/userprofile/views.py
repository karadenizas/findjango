from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from userprofile.forms import UserCreationForm


def profile(request):
    return render(request, 'userprofile/profile.html')


class RegisterCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/'
