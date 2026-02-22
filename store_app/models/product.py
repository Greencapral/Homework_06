from django.db import models

from store_app.models import BaseModel
from .category import Category


class Product(BaseModel):
    price = models.FloatField()
    category = models.ForeignKey(
        Category,
        related_name="products",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )
