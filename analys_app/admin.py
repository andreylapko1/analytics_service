from django.contrib import admin
from analys_app.models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_discount_price', 'product_rate', 'review_count')
    # readonly_fields = ('product_name', 'product_price' , 'product_discount_price', 'review_count', 'category', 'parsed_at', 'product_rate')
    search_fields = ('product_name', 'product_price', 'product_discount_price', 'product_rate')
    ordering = ('-parsed_at',)
    list_filter = ('category',)

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'products_count',)
    search_fields = ('category_name',)
    readonly_fields = ('category_name', 'products_count',)
# Register your models here.
