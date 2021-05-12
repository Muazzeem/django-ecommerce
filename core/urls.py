from django.urls import path

from address.views import CheckoutView
from order.views import add_to_basket, remove_from_basket, \
    remove_single_item_from_basket, DownloadPDF, OrderSummaryView
from thank_you.views import ThankYouView
from .views import (
    HomeView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_basket, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_basket, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_basket,
         name='remove-single-item-from-cart'),
    path('thank-you/', ThankYouView.as_view(), name='thank-you'),
    path('pdf_download/', DownloadPDF.as_view(), name="pdf_download"),
]
