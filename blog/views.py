from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET

from .models import User, WallPost
from .forms import RegistrationForm, LoginForm, New_wal_postForm
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

            User.objects.create_user(first_name=name, email=email, last_name=lastname, password=password)

            return redirect('authorization')
        else:
            return HttpResponse("не корректный ввод")

    elif request.method == 'GET':
        return render(request, "blog/registration.html")


def authorization(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                auth.login(request, user)
                return redirect("my_pag")
            else:
                return render(request, "blog/authorization.html",
                              context={"error_message": "Неверный логин или пароль"})
        else:
            return HttpResponse("не корректный ввод")
    elif request.method == 'GET':
        return render(request, "blog/authorization.html")


def my_pag(request):
    wall_post = WallPost.objects.filter(user_id=request.user.id)
    return render(request, "blog/my_pag.html", {'user': request.user, 'wall_post': [w.dict() for w in wall_post]})


def new_wal_post(request):
    if request.method == "POST":
        form = New_wal_postForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            WallPost.objects.create(text=text, user_id=request.user.id)
    return redirect('my_pag')


@require_POST
@login_required
def log_out(request):
    logout(request)
    return redirect('index')


@require_GET
def friends(request):
    friends_list = User.objects.filter().exclude(id=request.user.id)
    return render(request, 'blog/friends.html', {'friendsList': friends_list})


def friend(request, friend_id):
    user = User.objects.filter(id=friend_id).first()
    post = WallPost.objects.filter(user_id=friend_id)
    return render(request, "blog/friend_page.html", {"friend": user, "user_post": [w.dict() for w in post]})

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
