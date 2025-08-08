from django.test import TestCase
from django.urls import reverse
from .models import MenuItem  # Replace with your actual menu model name

class HomePageViewTest(TestCase):
    def setUp(self):
        # Create some menu items for testing
        MenuItem.objects.create(name="Test Pizza", price=250, description="Cheesy goodness")
        MenuItem.objects.create(name="Test Pasta", price=350, description="Creamy delight")

    def test_homepage_displays_menu(self):
        """
        Homepage should load successfully and contain menu items.
        """
        url = reverse('home')  # This should match the name in urls.py
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Pizza")
        self.assertContains(response, "Test Pasta")
