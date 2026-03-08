from math import ceil

from django.contrib import admin
from store_app.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "category",
        "created_at",
        "updated_at",
    )
    list_filter = ("category",)
    search_fields = ("name",)
    search_help_text = (
        "Введите наименование товара для поиска"
    )
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")
    fields = (
        "name",
        "price",
        "category",
    )

    @admin.action(description="изменить цену на 10%%")
    def price_increment(self, request, queryset):
        for product in queryset:
            product.price = round(product.price * 1.10, 2)
            product.save()

    actions = [
        price_increment,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
        "updated_at",
    )
    search_fields = ("name",)
    search_help_text = (
        "Введите наименование категории товара для поиска"
    )
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")
    fields = ("name",)
