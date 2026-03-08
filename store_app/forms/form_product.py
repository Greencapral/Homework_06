from django.forms import ModelForm
from store_app.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "price",
        ]
        labels = {
            "name": "Название товара",
            "description": "Описание товара",
            "category": "Категория товара",
            "price": "Цена за единицу",
        }
