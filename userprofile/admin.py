from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from userprofile.models import MyUser, Profile
from userprofile.forms import UserChangeForm, UserCreationForm


@admin.register(MyUser)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'user_name', 'is_admin', 'join_date')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('email', 'user_name')
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']