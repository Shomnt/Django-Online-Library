from django.contrib import admin
from .models import Author, BookAuthor, Book, BookGenre, BookTags, Comment, Genre, ProposeDelete, Tags, User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreateForm, CustomUserChangeForm


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        ('Information', {'fields': ('username', 'email', 'role')}),
        ('Status', {'fields': ('banned', 'is_active')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ()
    exclude = ('first_name', 'last_name')
    list_display = ['id_user', 'username', 'email', 'role', 'banned', 'is_active']


#admin.site.register(Author)
#admin.site.register(BookAuthor)
#admin.site.register(Book)
#admin.site.register(BookGenre)
#admin.site.register(BookTags)
#admin.site.register(Comment)
#admin.site.register(Genre)
#admin.site.register(ProposeDelete)
#admin.site.register(Tags)
admin.site.register(User, UserAdmin)
#admin.site.unregister(Group)
