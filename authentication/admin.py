from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name','is_active')
    list_filter = ('is_active', 'username')
    fields = [('email', 'password'), ('username', 'phone_number'), ('first_name', 'last_name')]

admin.site.register(User, UserAdmin)