from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='product name', null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='product price', null=True, blank=True)
    product_discount_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='product discount price', null=True, blank=True)
    product_rate = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='product_rate', null=True, blank=True)
    review_count = models.IntegerField( verbose_name='reviews count', null=True, blank=True)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, verbose_name='category', null=True, blank=True)
    parsed_at = models.DateTimeField(verbose_name='parsed at', auto_now_add=True, null=True, blank=True)


    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-parsed_at']

    def __str__(self):
        return self.product_name


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='product category', null=True, blank=True)
    products_count = models.IntegerField( verbose_name='products count', null=True, blank=True, default=0)

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'

    def __str__(self):
        return self.category_name

# Create your models here.
