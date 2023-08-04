from django.contrib import admin
from django.contrib.auth import get_user_model

from football_lovers.accounts.forms import EditUserForm, RegisterUserForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    form = EditUserForm
    add_form = RegisterUserForm

    ordering = ('id',)
    list_display = ('id', 'username', 'first_name', 'last_name', 'gender', 'email',)
    fieldsets = (
        (None,
         {
            'fields': ('username', 'password'),
         }),

        ('Personal Information',
         {
             'fields': ('first_name', 'last_name', 'email', 'gender', 'profile_picture'),
         }),

        ('Permissions',
         {
             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
         }),

        ('Date information',
         {
             'fields': ('last_login', 'date_joined'),
         }),
    )
