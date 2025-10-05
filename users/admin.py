from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )
    list_display = ('id','username', 'email','phone', 'role', 'is_staff', 'is_active','first_name','last_name','date_joined','updated_at','last_login','is_superuser','password')
    list_filter = ('role', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name','date_joined','updated_at','last_login')

admin.site.register(User, CustomUserAdmin)
