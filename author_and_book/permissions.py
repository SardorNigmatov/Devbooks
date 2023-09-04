from rest_framework.permissions import BasePermission

class CreateUpdatePersmissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.roles == 1

class CreateBookPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.roles in (1,3)
