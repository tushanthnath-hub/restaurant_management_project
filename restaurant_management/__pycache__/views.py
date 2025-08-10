from django.shortcuts import render

def menu_list(request):
    # Temporary hardcoded menu items
    menu_items = [
        {"name": "Margherita Pizza", "price": 299},
        {"name": "Paneer Tikka", "price": 249},
        {"name": "Pasta Alfredo", "price": 349},
        {"name": "Veg Burger", "price": 199},
    ]
    return render(request, 'menu_list.html', {'menu_items': menu_items})