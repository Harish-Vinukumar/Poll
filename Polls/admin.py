from django.contrib import admin

# Register your models here.

from .models import Questions, Choice, LoginCredentials

admin.site.register(Questions)
admin.site.register(Choice)
admin.site.register(LoginCredentials)
