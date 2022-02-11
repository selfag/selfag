from posixpath import split
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import Pensioner
from datetime import datetime, date



# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def add_new(request):
    if request.method=="POST":
        name=request.POST['name']
        pay=request.POST['pay']
        '''dob=request.POST['dob']
        doa=request.POST['doa']
        dor=request.POST['dor']'''
        d1,m1,y1= [int(x) for x in request.POST['dob'].split('/')]
        d2,m2,y2= [int(x) for x in request.POST['doa'].split('/')]
        d3,m3,y3= [int(x) for x in request.POST['dor'].split('/')]
        db=date(y1,m1,d1)
        da=date(y2,m2,d2)
        dr=date(y3,m3,d3)
        
        new_pensioner=Pensioner.objects.create(name=name, pay=pay, dob=db, doa=da, dor=dr)
        new_pensioner.save()
        pensioner=Pensioner.objects.all()
        return render(request, 'home.html', {'pensioner': pensioner})
    else:
        return render(request, 'add_new.html')

def home(request):
    pensioner=Pensioner.objects.all()
    return render(request, 'home.html', {'pensioner': pensioner}) 
   

    