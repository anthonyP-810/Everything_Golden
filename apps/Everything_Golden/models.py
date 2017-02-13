from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    email = models.EmailField(default='Update')
    password = models.CharField(max_length=40, null=True)
    password_confirmation = models.CharField(max_length=40, null=True)
    age = models.IntegerField(default='0', null=True)
    gender = models.CharField(max_length=1, null=True)
    phone = models.CharField(max_length=10, null=True) 
    membership_type = models.IntegerField(null=True)
    role = models.CharField(max_length=1, default='0')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return unicode(self.first_name + " " + self.last_name)

class Product(models.Model):
    description = models.CharField(max_length=70, null=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    orders = models.ManyToManyField(User, related_name="User_Orders")


class Event(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, default="")
    date_event = models.DateField()
    attendee = models.ManyToManyField(User, related_name="Event_Attendees")
    def __str__(self):
        return unicode(self.title + " " + str(self.date_event))



