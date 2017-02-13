from django.contrib import admin
from .models import Event, User, Product

# Register your models here.
@admin.register(Event, User, Product)
class EventAdmin(admin.ModelAdmin):
    pass

