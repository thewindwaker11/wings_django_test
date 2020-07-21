from django.contrib import admin

from .models import Category, Book, OrderItem, Order


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(OrderItem)
admin.site.register(Order)
