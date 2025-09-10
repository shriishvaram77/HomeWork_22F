from .models import Product
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = ['product_name', 'price', 'product_description', 'category']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_details')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['product_name', 'price', 'product_description', 'category']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:products')


class ContactUsView(TemplateView):
    fields = ['name', 'email', 'message']
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:contacts')
