from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authorization/', include('blog.urls')),
    path('registration/', include('blog.urls')),
    path('my_page/', include('blog.urls')),
    path('news/', include('blog.urls')),
    path('my_messages/', include('blog.urls')),
    path('documents/', include('blog.urls')),
    ]
