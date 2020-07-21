from django.urls import path

from store.services import add_to_cart, remove_from_cart, decrease_quantity_from_cart
from store.views import book_list, BookDetailView, OrderSummaryView

urlpatterns = [
    path('', book_list, name='book-list'),
    path('book/<slug>/', BookDetailView.as_view(), name='book'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),

    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', remove_from_cart, name="remove-from-cart"),
    path('decreace-quantity-from-cart/<slug>/', decrease_quantity_from_cart, name="decrease-quantity-from-cart"),
]
