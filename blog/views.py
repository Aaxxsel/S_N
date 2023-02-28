from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm


def index(request):
    return render(request, "blog/index.html", )


def registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            return HttpResponse(f"<h2>Добро пожаловать, {name}</h2>")
        else:
            return HttpResponse("не корректный ввод")
    else:
        form = User()
        return render(request, "blog/registration.html", {"form": form})

# def my_page(request):
#     return render(request, "blog/my_pag.html")
#
#
# def news(request):
#     return render(request, "blog/news.html")
#
#
# def my_messages(request):
#     return render(request, "blog/my_messages.html")
#
#
# def documents(request):
#     return render(request, "blog/documents.html")
