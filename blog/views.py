from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import RegistrationForm, LoginForm
from django.shortcuts import redirect


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
            user = User.objects.create(first_name=name, email=email, last_name=lastname, password=password)

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
                return HttpResponse(f"добро пожаловать {user.first_name}")
            else:
                return HttpResponse("Пользователь не найден")
        else:
            return HttpResponse("не корректный ввод")
    elif request.method == 'GET':
        return render(request, "blog/authorization.html")

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
