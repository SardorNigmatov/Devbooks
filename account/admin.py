from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username','first_name', 'last_name','phone',"email", "roles",)
    list_filter = ("username", 'first_name', 'last_name','phone',"email", "roles",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username","email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", 'roles',
            )}
        ),
    )
    search_fields = ("username","email")
    ordering = ("username","email")


admin.site.register(CustomUser, CustomUserAdmin)
