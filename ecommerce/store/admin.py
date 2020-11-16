from django.contrib import admin

# Register your models here.
from store.models import Customer, ShippingAddress, OrderItem, Product, Order

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

