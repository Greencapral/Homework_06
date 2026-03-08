from django.forms import ModelForm
from store_app.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "description",
        ]
        labels = {
            "name": "Название категории",
            "description": "Описание категории",
        }
