from django.contrib import admin
from .models import Customer, DateActivity, DateType

# Register your models here.
admin.site.register(Customer)
admin.site.register(DateActivity)
admin.site.register(DateType)