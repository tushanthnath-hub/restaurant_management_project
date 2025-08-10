from django.shortcuts import render

def contact_us(request):
    contact_info = {
        "phone": "+91 98765 43210",
        "email": "contact@tastybites.com",
        "address": "123, Food Street, Hyderabad, India"
    }
    return render(request, 'contact.html', {'contact_info': contact_info})