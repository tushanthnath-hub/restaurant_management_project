from django.test import TestCase
from django.contrib.auth.models import User
from .models import MenuItem, Order, OrderItem
from decimal import Decimal

class OrderModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create some menu items
        self.pizza = MenuItem.objects.create(name="Pizza", price=Decimal("250.00"), description="Cheesy goodness")
        self.pasta = MenuItem.objects.create(name="Pasta", price=Decimal("350.00"), description="Creamy delight")

        # Create an order
        self.order = Order.objects.create(
            customer=self.user,
            total_amount=Decimal("600.00"),
            status="PENDING"
        )

        # Add items to the order
        OrderItem.objects.create(order=self.order, menu_item=self.pizza, quantity=1)
        OrderItem.objects.create(order=self.order, menu_item=self.pasta, quantity=1)

    def test_order_creation(self):
        """Test that an order is created correctly with items."""
        self.assertEqual(self.order.customer.username, "testuser")
        self.assertEqual(self.order.order_items.count(), 2)
        self.assertEqual(self.order.total_amount, Decimal("600.00"))

    def test_order_items_quantity(self):
        """Test that order items have correct quantities."""
        pizza_item = OrderItem.objects.get(order=self.order, menu_item=self.pizza)
        pasta_item = OrderItem.objects.get(order=self.order, menu_item=self.pasta)

        self.assertEqual(pizza_item.quantity, 1)
        self.assertEqual(pasta_item.quantity, 1)
