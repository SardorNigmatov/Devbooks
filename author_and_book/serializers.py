from rest_framework import serializers
from .models import AuthorModel, BookModel

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['first_name','last_name','date_of_birth','date_of_death','country','genre','bio','image']


class CategoryAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['first_name','last_name','image','date_of_birth','date_of_death','genre']

class CategoryBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['title','pages','price','year','about_book','image','genre']


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['title','pages','year','price','genre','about_book','image','author']




