from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Главная страница.")


def about(request):
    return HttpResponse("Страница о нас")
