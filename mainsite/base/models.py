from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class Author(models.Model):
    id_author = models.IntegerField(db_column='ID_Author', primary_key=True)  # Field name made lowercase.
    author_name = models.TextField(db_column='Author_Name')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Author'


class Book(models.Model):
    id_book = models.IntegerField(db_column='ID_Book', primary_key=True)  # Field name made lowercase.
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='ID_User')  # Field name made lowercase.
    approved = models.BooleanField(db_column='Approved')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Book'


class BookAuthor(models.Model):
    book_id_book = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_ID_Book')  # Field name made lowercase.
    author_id_author = models.ForeignKey(Author, models.DO_NOTHING,
                                         db_column='Author_ID_Author')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Book_Author'


class BookGenre(models.Model):
    book_id_book = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_ID_Book')  # Field name made lowercase.
    genre_id_genre = models.ForeignKey('Genre', models.DO_NOTHING,
                                       db_column='Genre_ID_Genre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Book_Genre'


class BookTags(models.Model):
    book_id_book = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_ID_Book')  # Field name made lowercase.
    tags_id_tag = models.ForeignKey('Tags', models.DO_NOTHING, db_column='Tags_ID_Tag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Book_Tags'


class Comment(models.Model):
    id_comment = models.IntegerField(db_column='ID_Comment', primary_key=True)  # Field name made lowercase.
    text_comment = models.TextField(db_column='Text_Comment')  # Field name made lowercase. This field type is a guess.
    positive_rate = models.IntegerField(db_column='Positive_rate')  # Field name made lowercase.
    negative_rate = models.IntegerField(db_column='Negative_rate')  # Field name made lowercase.
    id_book = models.ForeignKey(Book, models.DO_NOTHING, db_column='ID_Book')  # Field name made lowercase.
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='ID_User')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comment'


class Genre(models.Model):
    id_genre = models.IntegerField(db_column='ID_Genre', primary_key=True)  # Field name made lowercase.
    genre_name = models.TextField(db_column='Genre_Name')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Genre'


class ProposeDelete(models.Model):
    id_propose = models.IntegerField(db_column='ID_Propose', primary_key=True)  # Field name made lowercase.
    id_book = models.ForeignKey(Book, models.DO_NOTHING, db_column='ID_Book')  # Field name made lowercase.
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='ID_User')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Propose_Delete'


class Tags(models.Model):
    id_tag = models.IntegerField(db_column='ID_Tag', primary_key=True)  # Field name made lowercase.
    tag_name = models.TextField(db_column='Tag_Name')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Tags'


class CustomUserManager(BaseUserManager):
    def _create_user(self, id_user, username, password, **extra_fields):
        if not password:
            raise ValueError("Нет пароля")
        user = self.model(id_user=id_user, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, id_user, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(id_user, username, password, **extra_fields)

    def create_superuser(self, id_user, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(id_user, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.IntegerField(db_column='Id_User', primary_key=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username',
                                default="", unique=True)  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email', unique=True,
                             default='')  # Field name made lowercase. This field type is a guess.
    password = models.TextField(db_column='Password')  # Field name made lowercase. This field type is a guess.
    role = models.SmallIntegerField(db_column='Role', default=1)  # Field name made lowercase.
    confermed = models.BooleanField(db_column='Confermed', default=False)  # Field name made lowercase.
    banned = models.BooleanField(db_column='Banned', default=False)  # Field name made lowercase.
    id_book_read = models.TextField(db_column='ID_Book_Read', blank=True,
                                    null=True)  # Field name made lowercase. This field type is a guess.
    id_book_readen = models.TextField(db_column='ID_Book_Readen', blank=True,
                                      null=True)  # Field name made lowercase. This field type is a guess.
    id_book_planning = models.TextField(db_column='ID_Book_Planning', blank=True,
                                        null=True)  # Field name made lowercase. This field type is a guess.
    id_book_dropped = models.TextField(db_column='ID_Book_Dropped', blank=True,
                                       null=True)  # Field name made lowercase. This field type is a guess.

    is_active = models.BooleanField(db_column='is_active', default=True)
    is_superuser = models.BooleanField(db_column='is_superuser', default=False)
    is_staff = models.BooleanField(db_column='is_staff', default=False)

    date_joined = models.DateTimeField(db_column='date_joined', default=timezone.now)
    last_login = models.DateTimeField(db_column='last_login', blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'id_user'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'email']

    class Meta:
        managed = False
        db_table = 'User'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username or str(self.email).split('@')[0]

    def __str__(self):
        return self.username