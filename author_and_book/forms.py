from django import forms
from .models import AuthorModel, BookModel

class AuthorForms(forms.ModelForm):
    genre_uz = forms.CharField()
    genre_en = forms.CharField(required=False)
    genre_ru = forms.CharField(required=False)

    bio_uz = forms.CharField()
    bio_en = forms.CharField(required=False)
    bio_ru = forms.CharField(required=False)


    class Meta:
        model = AuthorModel
        exclude = ['genre','bio']

class BookForm(forms.ModelForm):
    title_uz = forms.CharField()
    title_en = forms.CharField(required=False)
    title_ru = forms.CharField(required=False)

    about_book_uz = forms.CharField()
    about_book_en = forms.CharField(required=False)
    about_book_ru = forms.CharField(required=False)

    class Meta:
        model = BookModel
        exclude = ['title','about_book']





