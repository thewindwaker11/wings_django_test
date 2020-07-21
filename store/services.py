from django.contrib import messages
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

from store.models import Book, OrderItem, Order


def add_to_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    order_item, created_at = OrderItem.objects.get_or_create(book=book, user=request.user, is_ordered=False)
    order_queryset = Order.objects.filter(user=request.user, is_ordered=False)
    if order_queryset.exists():
        order = order_queryset[0]
        if order.books.filter(book__slug=book.slug).exists():
            order_item.quantity = F('quantity') + 1
            order_item.save()
            messages.info(request, "This Book quantity was updated")
        else:
            order.books.add(order_item)
    else:
        order = Order.objects.create(user=request.user, ordered_date=timezone.now())
        order.books.add(order_item)
    return redirect("book-list")
