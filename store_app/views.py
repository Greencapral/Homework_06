from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from store_app.forms import ProductForm, CategoryForm
from store_app.models import Product, Category


# Create your views here.
def index(request):
    return render(request, "store_app/main_page.html")


def about(request):
    return render(request, "store_app/about_page.html")


def products_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(
        request,
        "store_app/products_list.html",
        context=context,
    )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        "product": product,
    }
    return render(
        request,
        "store_app/product_detail.html",
        context=context,
    )


def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data[
                    "description"
                ],
                price=form.cleaned_data["price"],
                category=form.cleaned_data["category"],
            )
            return redirect("products_list")
    else:
        form = ProductForm()
        context = {
            "form": form,
        }
        return render(
            request,
            "store_app/product_add.html",
            context=context,
        )


def categories_list(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(
        request,
        "store_app/categories_list.html",
        context=context,
    )


def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data[
                    "description"
                ],
            )
            return redirect("categories_list")
    else:
        form = CategoryForm()
        context = {
            "form": form,
        }
        return render(
            request,
            "store_app/category_add.html",
            context=context,
        )
