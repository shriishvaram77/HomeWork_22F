from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


#def home(request):
    #return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено!")

    return render(request, 'catalog/contacts.html')


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_details.html', context=context)

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/home.html', context=context)


