from django.contrib import admin

# Register your models here.
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'email', 'mobile']

admin.site.register(CustomUser, UserAdmin)
