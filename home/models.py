from django.db import models
from django.shortcuts import render

def home(request):
    # Replace with your actual API endpoint
    api_url = "http://127.0.0.1:8000/api/menu/"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        menu_items = response.json()
    else:
        menu_items = []

    return render(request, 'home.html', {'menu_items': menu_items})
