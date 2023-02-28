from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index),
    path('registration/', views.registration, name="registration"),
    path('authorization/', views.authorization, name="authorization"),
    #     path('my_page/', views.my_page),
    #     path('news/', views.news),
    #     path('my_messages/', views.my_messages),
    #     path('documents/', views.documents),
]
