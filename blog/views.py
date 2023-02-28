from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import RegistrationForm, LoginForm
from django.shortcuts import redirect
from django.template import Context, Template


def index(request):
    return render(request, "blog/index.html", )


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            lastname = form.cleaned_data["lastname"]
            password_conf = form.cleaned_data["password_conf"]
            if password != password_conf:
                return render(request, "blog/registration.html", context={"error_message": "пароли не совпадает"})
            user = User.objects.filter(email=email)
            if user:
                return render(request, "blog/registration.html",
                              context={"error_email": "этот email уже занят"})

            User.objects.create(first_name=name, email=email, last_name=lastname, password=password)

            return redirect(authorization)
        else:
            return HttpResponse("не корректный ввод")

    elif request.method == 'GET':
        return render(request, "blog/registration.html")


def authorization(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.filter(email=email, password=password).first()
            if user:
                return redirect(my_pag)
            else:
                return render(request, "blog/authorization.html",
                              context={"error_message": "Неверный логин или пароль"})
        else:
            return HttpResponse("не корректный ввод")
    elif request.method == 'GET':
        return render(request, "blog/authorization.html")


def my_pag(request):
    men = ['Главная страница', 'cообщения', 'друзья', 'новости', 'документы']
    return render(request, "blog/my_pag.html", {'men': men})
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
