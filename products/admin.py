from django.contrib import admin
from .models import MenuItem, Order, OrderItem

# Custom admin for menu items
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
    list_filter = ('price',)


# Inline order items in the order view
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


# Custom admin for orders
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username',)
    inlines = [OrderItemInline]