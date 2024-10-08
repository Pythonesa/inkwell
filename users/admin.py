from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'birth_date')
    list_filter = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'birth_date', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'birth_date')