from django.shortcuts import render
from django.views.generic import TemplateView, View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from analys_app.filters import ProductFilter
from analys_app.models import Product
from analys_app.serializers import ProductListSerializer
from analys_app.utils.wb_parser import wb_category_parser


class HomeView(TemplateView):
    template_name = 'analys_app/base.html'



class BaseFormView(View):
    def post(self, request, *args, **kwargs):
        category_name = request.POST.get('category_name')
        parsing_pages = request.POST.get('page_count')
        try:
            pages = int(parsing_pages)
        except ValueError:
            pages = 3
        wb = wb_category_parser(category_name, pages)
        print(category_name, pages)

        return render(request,'analys_app/base.html')



class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['product_price', 'product_rate', 'review_count', ]


# Create your views here.
