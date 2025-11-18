from django.shortcuts import render
from .models import ProductModel, ProductStatusType
from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
)


class ShopProductGridView(ListView):
    template_name = "shop/product-grid.html"
    queryset = ProductModel.objects.filter(status=ProductStatusType.publish.value)
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        return context
