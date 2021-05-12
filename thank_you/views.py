from django.views.generic import TemplateView
from qr_code.qrcode.utils import ContactDetail

from core.models import Order


class ThankYouView(TemplateView):
    template_name = 'thank_you.html'

    def get_context_data(self, **kwargs):
        data = super(ThankYouView, self).get_context_data(**kwargs)
        order = Order.objects.all().first()
        user_address = order.shipping_address
        data['order'] = order
        data["contact_detail"] = ContactDetail(
            first_name=user_address.name,
            email=user_address.email,
            tel=user_address.phone,
        )
        return data
