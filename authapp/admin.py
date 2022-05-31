from django.contrib import admin
from authapp import models

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "user_name", "email", "is_active", "date_joined"]
    ordering = ["-date_joined"]