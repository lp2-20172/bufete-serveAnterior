from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Persona, Trabajador


# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(Persona)
admin.site.register(Trabajador)