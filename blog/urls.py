from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('authorization/', views.authorization, name="authorization"),
    path('my_pag/', views.my_pag, name="my_pag"),
    path('new_wal_post/', views.new_wal_post, name="new_wal_post"),
    path('log_out/', views.log_out, name="log_out"),
    path('friends/', views.friends, name="friends"),
    path('friend/<int:friend_id>/', views.friend, name="friend"),
    # path('my_messages/', views.my_messages),
    #     path('news/', views.news),
    #     path('documents/', views.documents),
]
