from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class Author(models.Model):
    author_name = models.CharField(max_length=255, null=False, blank=False)


class Genre(models.Model):
    genre_name = models.CharField(max_length=255, null=False, blank=False)


class Tags(models.Model):
    tag_name = models.CharField(max_length=255, null=False, blank=False)


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    name = models.CharField(max_length=255, null=False, blank=False, default="Неизвестно")
    rate = models.FloatField(null=False, blank=False, default=0.0)
    description = models.CharField(max_length=700, null=False, blank=True, default="")
    genres = models.ManyToManyField(Genre)
    tags = models.ManyToManyField(Tags)
    approved = models.BooleanField(default=False)


class Comment(models.Model):
    text_comment = models.CharField(max_length=700, null=False, blank=False)
    comment_rate = models.IntegerField(default=0)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)


class ProposeDelete(models.Model):
    book = models.ForeignKey('Book', models.CASCADE)
    user = models.ForeignKey('User', models.CASCADE)
    reason = models.CharField(max_length=700, null=False, blank=True, default="")


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not password:
            raise ValueError("Нет пароля")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    banned = models.BooleanField(default=False)
    books_reading = models.ManyToManyField(Book, related_name="Читаю", blank=True)
    book_read = models.ManyToManyField(Book, related_name="Прочитано", blank=True)
    book_planning = models.ManyToManyField(Book, related_name="Планнирую", blank=True)
    book_dropped = models.ManyToManyField(Book, related_name="Брошено", blank=True)

    objects = CustomUserManager()
    REQUIRED_FIELDS = []
