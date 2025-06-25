from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from .models import Product, ProductCategory

@receiver(post_save, sender=Product)
def update_category_product_count_save(sender, instance, created, **kwargs):
    if instance.category:
        if created:
            ProductCategory.objects.filter(id=instance.category.id).update(products_count=F('products_count') + 1)



@receiver(post_delete, sender=Product)
def update_category_product_delete(sender, instance, **kwargs):
    if instance.category:
        ProductCategory.objects.filter(id=instance.category.id).update(products_count=F('products_count') - 1)