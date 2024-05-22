from django.contrib import admin
from .models import Author, BookAuthor, Book, BookGenre, BookTags, Comment, Genre, ProposeDelete, Tags, User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        # Other fieldsets
        ('Permissions', {'fields': ('role', 'username', 'email', 'banned', 'confermed')}),
    )
    exclude = ('first_name', 'last_name')
    list_display = ['id_user', 'username', 'email', 'role', 'banned', 'confermed']


# Register your models here.
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Book)
admin.site.register(BookGenre)
admin.site.register(BookTags)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(ProposeDelete)
admin.site.register(Tags)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)