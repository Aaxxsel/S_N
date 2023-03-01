from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('authorization/', views.authorization, name="authorization"),
    path('my_pag/', views.my_pag, name="my_pag"),
    path('new_wal_post/', views.new_wal_post, name="new_wal_post"),
    path('log_out/', views.log_out, name="log_out"),
    #     path('news/', views.news),
    #     path('my_messages/', views.my_messages),
    #     path('documents/', views.documents),
]
