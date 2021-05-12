from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from address.forms import CheckoutForm
from core.models import BasketItem, Address, Order, Item


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class CheckoutView(View):

    def get(self, *args, **kwargs):
        try:
            item = BasketItem.objects.all()
            total = 0
            for order_item in item.all():
                total += order_item.get_final_price()
            context = {
                "order": item,
                "price": total,
            }
            return render(self.request, "checkout.html", context)

        except ObjectDoesNotExist:
            return redirect("core:home")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST)
        if form.is_valid():
            email = form.cleaned_data.get(
                'email')
            name = form.cleaned_data.get(
                'name')
            phone = form.cleaned_data.get(
                'phone')

            if is_valid_form([email, name, phone]):
                shipping_address = Address(
                    email=email,
                    name=name,
                    phone=phone,
                )
                shipping_address.save()
                BasketItem.objects.all()
                return redirect("core:thank-you")
        else:
            messages.info(self.request, "All fields are required.")
        return redirect("core:checkout")
