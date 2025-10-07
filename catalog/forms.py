from django import forms
from django.forms import BooleanField

from .models import Category, Product
from django.core.exceptions import ValidationError

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_description',]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'category', 'price', 'is_available']


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите наименование товара'
        })

        self.fields['product_description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену на товар'
        })

        self.fields['is_available'].widget.attrs.update({
            'class': 'form-check-input',
        })

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть меньше отрицательной')
        return price


    def clean(self):
        product_name = self.cleaned_data.get('product_name')
        product_description = self.cleaned_data.get('product_description')

        spam_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]

        for word in spam_words:
            if word in product_name:
                self.add_error('product_name','Данное слово нельзя использовать в этом поле')
            if word in product_description:
                self.add_error('product_description','Данное слово нельзя использовать в этом поле')



