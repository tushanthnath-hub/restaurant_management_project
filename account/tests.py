from django.test import TestCase
from django.urls import reverse
from .models import MenuItem  # Replace with your actual menu model name

class HomePageTest(TestCase):
    def setUp(self):
        # Create dummy menu items
        MenuItem.objects.create(name="Test Pizza", price=250, description="Cheesy goodness")
        MenuItem.objects.create(name="Test Pasta", price=350, description="Creamy delight")

    def test_homepage_loads_and_shows_menu(self):
        """
        Homepage should load successfully and display menu items.
        """
        url = reverse('home')  # This should match the name given in urls.py
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Pizza")
        self.assertContains(response, "Test Pasta")
