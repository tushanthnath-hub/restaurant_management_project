from django.shortcuts import render
from .models import MenuItem

def menu_view(request):
    menu_items = MenuItem.objects.all()
    context = {
        'menu_items': menu_items
    }
    return render(request, 'menu.html', context)