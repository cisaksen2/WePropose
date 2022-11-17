from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class DateCategory(models.Model):
    description = models.CharField(max_length=20)

    def __str__(self):
        return(self.description)

class Location(models.Model):
    date_category = models.OneToOneField(DateCategory, models.CASCADE)
    location_type = models.CharField(max_length=50)
    location_name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    main_photo = models.ImageField(upload_to='photos') #might wanna change this
    is_active = models.BooleanField(default=True)   #might wanna change this
    leave_date = models.DateField(default=datetime.today, blank=True)

    def __str__(self):
        return (self.title)

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13, blank = True)
    date_location = models.ManyToManyField(Location, blank=True)
    age = models.IntegerField(default = 18)
    residence_city = models.CharField(max_length=20)


    def __str__(self):
        return (self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    def save(self):
        self.first_name= self.first_name.upper()
        self.last_name= self.last_name.upper()
        super(Customer, self).save()