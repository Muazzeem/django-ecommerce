from django import template
from core.models import BasketItem

register = template.Library()


def cart_item_count():
    qs = BasketItem.objects.all()
    return qs[0].items.count()
