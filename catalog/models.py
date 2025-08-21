from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Наименование')
    category_description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'


    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование')
    product_description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    price = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    photo = models.ImageField(upload_to='photos/', verbose_name='Изображение')

    def __str__(self):
        return f'{self.product_name} {self.product_description} {self.category} {self.price}'


    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['product_name']
