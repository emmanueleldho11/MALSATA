from django.db import models

class OrderRegistration(models.Model):
    name = models.CharField(max_length=30)
    phoneno = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    veg_or_non = models.CharField(max_length=1, default='n')
    qty = models.IntegerField(default=1)
    def __str__(self):
        st = " %-30s %-15s %-250s %s %-2s " % (self.name, self.phoneno, self.address, self.veg_or_non, self.qty)
        return st


class FoodLocation(models.Model):
    name = models.CharField(max_length=30)
    phoneno = models.CharField(max_length=15)
    centre_name = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    veg_or_non = models.CharField(max_length=1, default='n')
    qty = models.IntegerField(default=1)
    wrk_hrs = models.CharField(max_length=4)
    def __str__(self):
        st = " %-30s %-15s %-30s %-250s %s %d %-20s " % (self.name, self.phoneno, self.centre_name, self.address, self.qty, self.veg_or_non, self.wrk_hrs)
        return st

    
class DeliveryBoy(models.Model):
    name = models.CharField(max_length=30)
    phoneno = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    wrk_hrs = models.CharField(max_length=15)
    def __str__(self):
        st = " %-30s %-15s %-250s %-20s " % (self.name, self.phoneno, self.address, self.wrk_hrs)
        return st
