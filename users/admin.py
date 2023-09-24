from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ["reg_no",'first_name',]
    ordering = ("reg_no",)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('reg_no', 'first_name', 'password1', 'password2'),}),)

    fieldsets = (
            (("Basic Info"), {"fields": ("reg_no", "password")}),
            (("Personal info"), {"fields": ("first_name",)}),
            (
                ("Permissions"),
                {
                    "fields": (
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            (("Important dates"), {"fields": ("last_login",)}),
            (("pic"),{"fields":("pic",)}),
        )
    
admin.site.register(get_user_model(),CustomUserAdmin)