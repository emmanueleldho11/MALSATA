from django import forms

from .models import OrderRegistration
from .models import FoodLocation
from .models import DeliveryBoy


class OrderRegistrationForm(forms.Form):
    name = forms.CharField(max_length=30, label = "Name of Authority")
    phoneno = forms.CharField(max_length=15, label = "Contact Number")
    address = forms.CharField(max_length=4, label = "Address with PinCode")

    veg_or_non_choices = [('Vegetarian','v'), ('Non-Vegiterian','n')]
    veg_or_non = forms.CharField(max_length=1, label = "Veg or Non-Veg", widget = forms.Select(choices = veg_or_non_choices))

    qty_choices = [('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10')]
    qty = forms.CharField(max_length=1, label = "Quanity of Food", widget = forms.Select(choices = qty_choices))
    
    hd_id = forms.CharField(widget = forms.HiddenInput(), initial = "0")


class FoodLocationForm(forms.Form):
    name = forms.CharField(max_length=30, label = "Name of Authority")
    phoneno = forms.CharField(max_length=15, label = "Contact Number")
    centre_name = forms.CharField(max_length=30, label = "Food Collection Point Name")
    address = forms.CharField(max_length=4, label = "Address with PinCode")

    veg_or_non_choices = [('Vegetarian','v'), ('Non-Vegiterian','n')]
    veg_or_non = forms.CharField(max_length=1, label = "Veg or Non-Veg", widget = forms.Select(choices = veg_or_non_choices))
                          
    qty_choices = [('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10')]
    qty = forms.CharField(max_length=1, label = "Quanity of Food", widget = forms.Select(choices = qty_choices))
    
    wrk_hrs = forms.CharField(max_length=4, label = "Work Hours")


class DeliveryBoyForm(forms.Form):
    name = forms.CharField(max_length=30, label = "Name of Applicant")
    phoneno = forms.CharField(max_length=15, label = "Contact Number")
    address = forms.CharField(max_length=4, label = "Address with PinCode")
    wrk_hrs = forms.CharField(max_length=4, label = "Work Hours")
