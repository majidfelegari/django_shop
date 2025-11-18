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

