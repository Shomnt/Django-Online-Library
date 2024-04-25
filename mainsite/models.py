from django.db import models


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
    author_id_author = models.ForeignKey(Author, models.DO_NOTHING, db_column='Author_ID_Author')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Book_Author'


class BookGenre(models.Model):
    book_id_book = models.ForeignKey(Book, models.DO_NOTHING, db_column='Book_ID_Book')  # Field name made lowercase.
    genre_id_genre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='Genre_ID_Genre')  # Field name made lowercase.

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


class User(models.Model):
    id_user = models.IntegerField(db_column='Id_User', primary_key=True)  # Field name made lowercase.
    nickname = models.TextField(db_column='Nickname')  # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email')  # Field name made lowercase. This field type is a guess.
    password = models.TextField(db_column='Password')  # Field name made lowercase. This field type is a guess.
    role = models.SmallIntegerField(db_column='Role')  # Field name made lowercase.
    confermed = models.BooleanField(db_column='Confermed')  # Field name made lowercase.
    banned = models.BooleanField(db_column='Banned')  # Field name made lowercase.
    id_book_read = models.TextField(db_column='ID_Book_Read', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_book_readen = models.TextField(db_column='ID_Book_Readen', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_book_planning = models.TextField(db_column='ID_Book_Planning', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    id_book_dropped = models.TextField(db_column='ID_Book_Dropped', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'User'
