from django.urls import path
#from catalog import views
from .views import ProductListView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductUpdateView, \
    ContactUsView

app_name = 'catalog'

urlpatterns = [

    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactUsView.as_view(), name='contacts'),

]