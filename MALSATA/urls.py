from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^home/', views.index, name = "HOME"),
    url(r'^$', views.abc, name = "HOME1"),
    url(r'^OrderRegistration/', views.saveOrderRegistrationData, name = "saveOrderRegistration"),
    path('delete/<int:odr_id>/', views.deleteOrderRegistrationData, name = "odr_del"),
    url(r'^FoodLocation/', views.saveFoodLocationData, name = "FoodLocation"),
    path('delete/<int:lcn_id>/', views.deleteFoodLocationData, name = "lcn_del"),
    url(r'^DeliveryBoyData/', views.saveDeliveryBoyData, name = "saveDeliveryBoy"),
    path('delete/<int:dlv_id>/', views.deleteDeliveryBoyData, name = "dlv_del"),
    
]
