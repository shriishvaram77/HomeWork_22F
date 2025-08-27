from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product_details/<int:pk>', views.product_details, name='product_details'),

]