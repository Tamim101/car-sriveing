from django.shortcuts import render

from django.http import HttpResponse
from .models import Car
from django.http import Http404
def home(request):
    cars = Car.objects.all
    return render(request,'todo/home.html',{'cars':cars})

def car_detail(request,id):
    try:
        car = Car.objects.get(id=id)
    except  Car.DoesNotExist:
        raise Http404('car not found')

    return render(request,'todo/car_detail.html',{'car':car})