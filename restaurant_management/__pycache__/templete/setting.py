from django.conf import settings
from django.shortcuts import render

def home(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'home.html', context)