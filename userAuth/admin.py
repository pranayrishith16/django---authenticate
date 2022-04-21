from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import AuthUser


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = AuthUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(AuthUser, CustomUserAdmin)