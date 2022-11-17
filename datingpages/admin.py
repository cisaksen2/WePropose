from django.contrib import admin
from .models import Customer, DateCategory, Location

# Register your models here.
admin.site.register(Customer)
admin.site.register(DateCategory)
admin.site.register(Location)
