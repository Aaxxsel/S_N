from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "blog/authorization_one.html",)


def registration(request):
    return render(request, "blog/registration.html")


def my_page(request):
    return render(request, "blog/my_pag.html")


def news(request):
    return render(request, "blog/news.html")


def my_messages(request):
    return render(request, "blog/my_messages.html")


def documents(request):
    return render(request, "blog/documents.html")


