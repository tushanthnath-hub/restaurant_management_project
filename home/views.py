from django.shortcuts import render
import requests

def home(request):
    api_url = "http://127.0.0.1:8000/api/menu/"  # Your API endpoint
    try:
        response = requests.get(api_url)
        menu_items = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        menu_items = []  # Fallback if API is down

    return render(request, 'home.html', {'menu_items': menu_items})
