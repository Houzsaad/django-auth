from django.contrib import admin

# Register your models here.

from .models import User, Memmber, CEO

admin.site.register(User)

admin.site.register(Memmber)

admin.site.register(CEO)
