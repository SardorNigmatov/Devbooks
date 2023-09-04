from django.urls import path
from .views import (ListAuthorView,
                    ListBookView,
                    CreateAuthorView,
                    DetailAuthorView,
                    UpdateAuthorView,
                    DeleteAuthorView,
                    CreateBookView,
                    DetailBookView,
                    UpdateBookView,
                    DeleteBookView,
                    CategoryAuthorView,
                    AuthorSearchView,
                    CategoryBookView,
                    BookSearchView,
                    )

urlpatterns = [
    path('author/',ListAuthorView.as_view(),name='author'),
    path('book/',ListBookView.as_view(),name='book'),
    path('author/create/',CreateAuthorView.as_view(),name='author_create'),
    path('author/detail/<int:pk>/',DetailAuthorView.as_view(),name='author_detail'),
    path('author/update/<int:pk>/',UpdateAuthorView.as_view(),name='author_update'),
    path('author/delete/<int:pk>/',DeleteAuthorView.as_view(),name='author_delete'),
    path('book/create/',CreateBookView.as_view(),name='book_create'),
    path('book/detail/<int:pk>/',DetailBookView.as_view(),name='book_detail'),
    path('book/update/<int:pk>/',UpdateBookView.as_view(),name='book_update'),
    path('book/delete/<int:pk>/',DeleteBookView.as_view(),name='book_delete'),
    path('category/author/<str:genre>/',CategoryAuthorView.as_view(),name='category_author'),
    path('author/search/', AuthorSearchView.as_view(),name='author_search'),
    path('category/book/<str:genre>/',CategoryBookView.as_view(),name='category_book'),
    path('book/search/',BookSearchView.as_view(),name='book_search')
]