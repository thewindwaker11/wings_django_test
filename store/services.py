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
            messages.info(request, "This book was added to your cart.")
    else:
        order = Order.objects.create(user=request.user, ordered_date=timezone.now())
        order.books.add(order_item)
        messages.info(request, "this book was added to your cart")

    return redirect("order-summary")


def remove_from_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    order_queryset = Order.objects.filter(user=request.user, is_ordered=False)

    if order_queryset.exists():
        order = order_queryset[0]

        if order.books.filter(book__slug=book.slug).exists():
            order_item = OrderItem.objects.filter(book=book, user=request.user, is_ordered=False)[0]
            order.books.remove(order_item)
            order_item.delete()
            messages.info(request, "This book has been removed from your cart.")
        else:
            # message "the user does not have an order
            messages.info(request, "This book is not in your cart.")
            return redirect("book-list")

    else:
        messages.info(request, "You do not have an active order.")

    return redirect("book-list")


def decrease_quantity_from_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    order_queryset = Order.objects.filter(user=request.user, is_ordered=False)

    if order_queryset.exists():
        order = order_queryset[0]

        if order.books.filter(book__slug=book.slug).exists():
            order_item = OrderItem.objects.filter(book=book, user=request.user, is_ordered=False)[0]

            if order_item.quantity > 1:
                order_item.quantity = F('quantity') - 1
                order_item.save()
                messages.info(request, "This book quantity was updated")
            else:
                order.books.remove(order_item)
                order_item.delete()
                messages.info(request, "This book was removed from your cart.")
        else:
            messages.info(request, "This book is not in your cart.")
    else:
        messages.info(request, "You don't have an active order.")

    return redirect("order-summary")
