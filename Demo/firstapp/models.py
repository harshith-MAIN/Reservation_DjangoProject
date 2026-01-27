from django.db import models


class MenuItems(models.Model):

    name = models.CharField(max_length=255)
    price = models.IntegerField()

# Create your models here.
class Reservation(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    guestcount = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField( max_length=250)