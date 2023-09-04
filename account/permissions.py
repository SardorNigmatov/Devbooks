from rest_framework.permissions import BasePermission


class MyProfilePermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return str(request.user) == str(obj.username)