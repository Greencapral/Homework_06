from django.db import models

from store_app.models import BaseModel
from .category import Category


class Product(BaseModel):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование товара",
    )
    price = models.FloatField(verbose_name="цена за ед.")
    category = models.ForeignKey(
        Category,
        related_name="products",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        verbose_name="товарная категория",
    )
