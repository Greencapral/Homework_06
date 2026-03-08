from django.db import models
from store_app.models import BaseModel


class Category(BaseModel):
    name = models.CharField(
        max_length=100,
        verbose_name="товарная категория",
    )
