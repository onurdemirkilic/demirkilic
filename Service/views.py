from django.shortcuts import render
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
# Create your views here.



def Shipment (request) : 
    return render(request,'shipment.html')

def ControlShipment (request) : 
    print("TEST")
    trackingnumber = request.GET.get("trackingNumber")
    context = { "shipment_status" : f"ONUR DEMIRKILIC {trackingmuber}",
               }
    return render(request,'shipment.html',context=context)


def Handler404 (request,exception) : 
    return render(request,"handler404.html")

def Handler500 (request) : 
    return render(request,"handler404.html")

def LoginService (request) : 
	return render(request,'login.html')

def login_request (request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        alogin(request, user)
        return render(request,'/admin')
        ...
    else:
        pass