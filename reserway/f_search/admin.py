from django.contrib import admin

# Register your models here.
from .models import Journey,Routes

admin.site.register(Journey)
admin.site.register(Routes)