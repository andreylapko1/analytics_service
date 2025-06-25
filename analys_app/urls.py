from django.urls import path
from analys_app.views import ProductListApiView, ProductDashboardView,BaseFormView

urlpatterns = [
    path('', BaseFormView.as_view(), name='base_view'),
    path('analys/', BaseFormView.as_view(), name='base_form_view'),
    path('analys/dashboard/', ProductDashboardView.as_view(), name='dashboard_view'),
    path('api/products/', ProductListApiView.as_view(), name='product_list'),
]