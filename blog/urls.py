from django.urls import path

from blog.views import authorization

urlpatterns = [
    path('', authorization),
    path('registration', registration),
    path('my_page', my_page),
    path('news', news),
    path('my_messages', my_messages),
    path('documents', documents),
]
