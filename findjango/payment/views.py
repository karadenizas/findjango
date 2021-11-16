from django.shortcuts import render


def purchasing_option(request):
    return render(request, 'payment/purchasing_option.html')