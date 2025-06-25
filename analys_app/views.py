from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView
from analys_app.filters import ProductFilter
from analys_app.models import Product, ProductCategory
from analys_app.serializers import ProductListSerializer
from analys_app.utils.wb_parser import wb_category_parser


class BaseFormView(View):
    template_name = 'analys_app/base.html'



    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        category_name = request.POST.get('category_name')
        parsing_pages = request.POST.get('page_count')
        try:
            pages = int(parsing_pages)
        except ValueError:
            pages = 3
        wb_category_parser(category_name, pages)
        request.session['category'] = category_name
        return redirect('dashboard_view')




class ProductDashboardView(View):
    template_name = 'analys_app/product_dashboard.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['product_price', 'product_rate', 'review_count', ]

    def get_queryset(self):
        qs = super().get_queryset()
        category_name = self.request.session.get('category')
        category_id = ProductCategory.objects.get(category_name=category_name).id
        return qs.filter(category=category_id)


# Create your views here.
