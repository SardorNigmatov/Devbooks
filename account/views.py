from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from .permissions import MyProfilePermissions
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomSerializer, MyProfileserializer, ChangePasswordSerializer
# Create your views here.

class CreateUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomSerializer


class MyProfileView(RetrieveUpdateAPIView):
    permission_classes = (MyProfilePermissions,)
    queryset = CustomUser.objects.all()
    serializer_class = MyProfileserializer


class ChangePasswordView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


