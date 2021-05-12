from io import BytesIO

from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from xhtml2pdf import pisa
from django.http import HttpResponse

from django.template.loader import get_template

from core.models import Item, BasketItem


def add_to_basket(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = BasketItem.objects.get_or_create(
        item=item,
    )
    product_quantity = BasketItem.objects.filter(item=item)
    product = product_quantity[0]
    product.quantity += 1
    product.save()
    return redirect("core:order-summary")


def remove_from_basket(request, slug):
    item = get_object_or_404(Item, slug=slug)
    BasketItem.objects.filter(item=item).delete()
    return redirect("core:order-summary")


def remove_single_item_from_basket(request, slug):
    item = get_object_or_404(Item, slug=slug)
    product_quantity = BasketItem.objects.filter(item=item)
    product = product_quantity[0]
    product.quantity -= 1
    product.save()
    if product.quantity < 1:
        BasketItem.objects.filter(item=item).delete()
    return redirect("core:order-summary")


def render_to_pdf(template_src, context_dict=None):
    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class OrderSummaryView(ListView):
    model = BasketItem
    template_name = "order_summary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = BasketItem.objects.all()
        return context


class DownloadPDF(DetailView):

    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('thank_you.html')

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % "12341231"
        content = "attachment; filename='%s'" % filename
        response['Content-Disposition'] = content
        return response
