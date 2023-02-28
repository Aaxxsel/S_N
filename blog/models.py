from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)


class WallPost(models.Model):
    text = models.CharField(max_length=500)
    dateTime = models.DateField(auto_now_add=True)
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)

# class Messages(models.Model):
#     sender = models.ForeignKey(to='User', on_delete=models.PROTECT)
#     recipient = models.ForeignKey(to='User', on_delete=models.PROTECT)
#     pick_up_time = models.DateField(auto_now=True)
#     text_messages = models.CharField(max_length=500)
#
#
# class Friends(models.Model):
#     friends_user = models.ForeignKey(to='User', on_delete=models.PROTECT)
