from django.contrib import admin
from .models import ProductModel, ProductCategoryModel, ProductImageModel, WishlistProductModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "stock", "status", "created_date")


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date")


@admin.register(ProductImageModel)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "created_date")

    
@admin.register(WishlistProductModel)
class WishlistProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")

