from .serializers import AuthorSerializer, Bookserializer, CategoryAuthorSerializer, CategoryBookSerializer
from .models import AuthorModel, BookModel
from rest_framework.response import Response
from .permissions import CreateUpdatePersmissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .paginations import CustomPagination
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView)


#Author  model
class ListAuthorView(ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

class DetailAuthorView(RetrieveAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)

class CreateAuthorView(CreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,CreateUpdatePersmissions)

class UpdateAuthorView(UpdateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,CreateUpdatePersmissions)

class DeleteAuthorView(DestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,CreateUpdatePersmissions)




#Book model

class ListBookView(ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = Bookserializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination


class DetailBookView(RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = Bookserializer
    permission_classes = (IsAuthenticated,)


class CreateBookView(CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = Bookserializer
    permission_classes = (IsAuthenticated,CreateUpdatePersmissions)

class UpdateBookView(UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = Bookserializer
    permission_classes = (IsAuthenticated,CreateUpdatePersmissions)

class DeleteBookView(DestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = Bookserializer
    permission_classes = (IsAuthenticated,CreateUpdatePersmissions)


class CategoryAuthorView(ListAPIView):
    serializer_class = CategoryAuthorSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    def get_queryset(self):
        genre = self.kwargs['genre']
        return AuthorModel.objects.filter(genre=genre)


class AuthorSearchView(APIView):
    serializer_class = AuthorSerializer
    def get(self, request):
        first_name = request.query_params.get('first_name', '')
        authors = AuthorModel.objects.filter(first_name__icontains=first_name)
        serializer = self.serializer_class(authors, many=True)
        return Response(serializer.data)


class CategoryBookView(ListAPIView):
    serializer_class = CategoryBookSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    def get_queryset(self):
        genre = self.kwargs['genre']
        return BookModel.objects.filter(genre=genre)


class BookSearchView(APIView):
    serializer_class = Bookserializer
    def get(self, request):
        title = request.query_params.get('title', '')
        authors = BookModel.objects.filter(title=title)
        serializer = self.serializer_class(authors, many=True)
        return Response(serializer.data)





