from django.contrib import admin
from .models import Author, Book, Comment, Genre, ProposeDelete, Tags, User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreateForm, CustomUserChangeForm


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        ('Information', {'fields': ('username', 'email', 'groups')}),
        ('Status', {'fields': ('banned', 'is_active')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
        ('Books', {'fields': ('books_reading', 'book_read', 'book_planning', 'book_dropped')})
    )
    filter_horizontal = ('groups', 'user_permissions')
    exclude = ('first_name', 'last_name')
    list_display = ['id', 'username', 'email', 'banned', 'is_active']


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(ProposeDelete)
admin.site.register(Tags)
admin.site.register(User, UserAdmin)
#admin.site.unregister(Group)
