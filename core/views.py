from django.views.generic import ListView

from .models import Item, Category
import json


class HomeView(ListView):
    model = Item
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # category = self.request.GET["category"]
        context['categories'] = Category.objects.all()
        category = []
        if category:
            context['items'] = Item.objects.filter(category__name="AAA")
        else:
            context['qs_json'] = json.dumps(list(Item.objects.values()))
        return context
