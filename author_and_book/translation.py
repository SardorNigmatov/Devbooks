from modeltranslation.translator import TranslationOptions, register
from .models import BookModel, AuthorModel


@register(BookModel)
class BookTranslation(TranslationOptions):
    fields = ('title','about_book')

@register(AuthorModel)
class AuthorTranslation(TranslationOptions):
    fields = ('genre','bio')
