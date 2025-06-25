from django.urls import path
from analys_app.views import HomeView, BaseFormView, ProductListApiView

urlpatterns = [
    path('', HomeView.as_view(), name='base_view'),
    path('products/', ProductListApiView.as_view(), name='product_list'),
    path('form/', BaseFormView.as_view(), name='base_form'),
]