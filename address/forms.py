from django import forms


class CheckoutForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
