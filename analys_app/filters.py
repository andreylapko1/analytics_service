import django_filters
from analys_app.models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='product_price', lookup_expr='gte')
    min_rating = django_filters.NumberFilter(field_name='product_rate', lookup_expr='gte')
    min_reviews = django_filters.NumberFilter(field_name='review_count', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='product_price', lookup_expr='lte')
    max_rating = django_filters.NumberFilter(field_name='product_price', lookup_expr='lte')
    max_reviews = django_filters.NumberFilter(field_name='review_count', lookup_expr='lte')


    class Meta:
        model = Product
        fields = ['product_price','product_rate', 'review_count']