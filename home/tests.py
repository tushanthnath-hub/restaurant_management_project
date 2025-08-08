from django.test import TestCase


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import MenuItem  # Replace with your actual model name

class MenuAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create some test menu items
        MenuItem.objects.create(name="Test Pizza", price=250, description="Test description")
        MenuItem.objects.create(name="Test Pasta", price=350, description="Test description")

    def test_menu_list(self):
        """
        Ensure the menu API returns the list of items.
        """
        url = reverse('menu-list')  # Use your actual DRF route name
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
        self.assertEqual(response.data[0]['name'], "Test Pizza")
