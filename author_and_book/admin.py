from django.contrib import admin
from .models import AuthorModel, BookModel


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','country','date_of_birth']
    search_fields = ['last_name','email','phone']


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','year','price','genre']
    search_fields = ['title','price','genre']

