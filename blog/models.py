from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        # Создает и сохраняет пользователя с введенным им email и паролем.

        if not email:
            raise ValueError('email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField('first_name', max_length=20)
    last_name = models.CharField('last_name', max_length=20)
    email = models.EmailField('email', unique=True)
    password = models.CharField('password', max_length=50)
    created_date = models.DateField('created_date', auto_now_add=True)
    is_active = models.BooleanField('is_active', default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    friends = models.ManyToManyField(to='User')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def dict(self) -> dict:
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,

        }


class WallPost(models.Model):
    text = models.CharField(max_length=500)
    dateTime = models.DateField(auto_now_add=True)
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)

    def dict(self) -> dict:
        return {
            "id": self.id,
            'text': self.text,
            'publish_date': self.dateTime,

        }

# class Messages(models.Model):
#     sender = models.ForeignKey(to='User', on_delete=models.PROTECT)
#     recipient = models.ForeignKey(to='User', on_delete=models.PROTECT)
#     pick_up_time = models.DateField(auto_now=True)
#     text_messages = models.CharField(max_length=500)
#
#
