from django.shortcuts import render

from .models import OrderRegistration
from .models import FoodLocation
from .models import DeliveryBoy

from .forms import OrderRegistrationForm
from .forms import FoodLocationForm
from .forms import DeliveryBoyForm

from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

# Create your views here.



def index(request):
    return HttpResponse("<h3> Hurray!!! </h3>")


def abc(request):
    return HttpResponse("<h1> Hi WELCOME! </h1>")


def saveOrderRegistrationData(request):
    if request.method == "POST":
        form = OrderRegistrationForm(request.POST)
        print(request.POST)
        print(form)
##        if form.is_vaild():
##        try:
        order_data = OrderRegistration(
            name = form.cleaned_data['name'],
            phoneno = form.cleaned_data['phoneno'],
            address = form.cleaned_data['address'],
            veg_or_non = form.cleaned_data['veg_or_non'].lower(),
            qty = form.cleaned_data['qty']
            )
        od_id = request.POST["hd_id"]
        if od_id != "0":
            order_data.phoneno = int(od_id)
        print(od_id, order_data.name)
        order_data.save()
        return HttpResponse("<h1> SUCCESSFULL </h1>")
        return HttpResponseRedirect("/details/OrderRegistration/")
##        except:
        return HttpResponse("<h1> Data Error !!! </h1>")
    else:
        form = OrderRegistrationForm()
    return render(request,"OrderRegistrationForm.html",{"OrderRegistrationForm":form})


def deleteOrderRegistrationData(request, odr_id):
    OrderRegistration.objects.get(id = odr_id).delete()
    return HttpResponse("<h1> SUCCESSFULL </h1>")
    return HttpResponseRedirect("/details/OrderRegistration/")
    #return HttpResponse("Deleted Order Registration Data ! <br/> <a href ='<h1> SUCCESSFULL </h1>'> </a>")


def saveFoodLocationData(request):
    if request.method == "POST":
        form = FoodLocationForm(request.POST)
        print(request.POST)
        print(form)
        loc_data = FoodLocation(
            name = form.cleaned_data['name'],
            phoneno = form.cleaned_data['phoneno'],
            centre_name = form.cleaned_data['centre_name'],
            address = form.cleaned_data['address'],
            veg_or_non = form.cleaned_data['veg_or_non'],
            qty = form.cleaned_data['qty'],
            wrk_hrs = form.cleaned_data['wrk_hrs']
            )
        loc_id = request.POST["hd_id"]
        if loc_id != "0":
            loc_data.phoneno = int(loc_id)
        print(loc_id, loc_data.name)
        loc_data.save()
        return HttpResponse("<h1> SUCCESSFULL </h1>")
        return HttpResponseRedirect("/details/FoodLocation/")
    
        return HttpResponse("<h1> Data Error !!! </h1>")
    else:
        form = FoodLocationForm()
    return render(request,"FoodLocationForm.html",{"FoodLocationForm":form})



def deleteFoodLocationData(request, lcn_id):
    FoodLocation.objects.get(id = lcn_id).delete()
    return HttpResponseRedirect("/details/FoodLocation/")


def saveDeliveryBoyData(request):
    if request.method == "POST":
        form = DeliveryBoyForm(request.POST)
        print(request.POST)
        print(form)
        del_data = DeliveryBoy(
            name = form.cleaned_data['name'],
            phoneno = form.cleaned_data['phoneno'],
            address = form.cleaned_data['address'],
            wrk_hrs = form.cleaned_data['wrk_hrs']
            )
        del_id = request.POST["hd_id"]
        if del_id != "0":
            del_data.phoneno = int(del_id)
        print(del_id, del_data.name)
        del_data.save()
        return HttpResponse("<h1> SUCCESSFULL </h1>")
        return HttpResponseRedirect("/details/DeliveryBoyData/")
    
        return HttpResponse("<h1> Data Error !!! </h1>")
    else:
        form = DeliveryBoyForm()
    return render(request,"DeliveryBoyForm.html",{"DeliveryBoyForm":form})


def deleteDeliveryBoyData(request, dlv_id):
    DeliveryBoy.objects.get(id = dlv_id).delete()
    return HttpResponseRedirect("/details/DeliveryBoyData/")

