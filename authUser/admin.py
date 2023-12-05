from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class AdminUser(admin.ModelAdmin):
    list_display = ["id", "username", "is_admin", "user_choice"]
