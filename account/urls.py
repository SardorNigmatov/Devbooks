from django.urls import path, include
from .views import CreateUserView, MyProfileView, ChangePasswordView

urlpatterns = [
    path('sign_up/',CreateUserView.as_view(),name='create'),
    path('myprofile/<str:pk>/',MyProfileView.as_view(),name='myprofile'),
    path('password/change/<int:pk>',ChangePasswordView.as_view(),name='change_password'),
]