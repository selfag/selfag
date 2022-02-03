from posixpath import split
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import Pensioner
from datetime import datetime, date
from dateutil import relativedelta


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def add_new(request):
    if request.method=="POST":
        name=request.POST['name']
        pay=request.POST['pay']
        dob=request.POST['dob']
        doa=request.POST['doa']
        dor=request.POST['dor']
        d1,m1,y1=[int(x) for x in request.POST['dob'].split('/')]
        dob=date(y1,m1,d1)
        d2,m2,y2=[int(x) for x in request.POST['doa'].split('/')]
        doa=date(y2,m2,d2)
        d3,m3,y3=[int(x) for x in request.POST['dor'].split('/')]
        dor=date(y3,m3,d3)

        def datediff(a,b):
            a=date(y2,m2,d2)
            b=date(y3,m3,d3)
            serv=relativedelta.relativedelta(b,a)
            nqs=serv.years
            if (serv.months>=6):
                nqs=nqs+1
            else:
                nqs=nqs
            return nqs
        qs=datediff(dor,dob)
        def age_pensioner(a,b):
            a=date(y1,m1,d1)
            b=date(y3,m3,d3)
            age_r=relativedelta.relativedelta(b,a)
            age_y=f"{age_r.years}Y-{age_r.months}M-{age_r.days}D"
            return age_y

        age=age_pensioner(dor,dob)

        def rate_anb(dor,dob):
            a=date(y1,m1,d1)
            b=date(y3,m3,d3)
            age_n=relativedelta.relativedelta(b,a)
            age_nb=age_n.years+1
            com_table2001 ={20:40.5043, 21:39.7341, 22:38.9653,23:38.1974,24:37.4307,25:36.6651,26:35.9006,27:35.1372,28:34.3750,29:33.6143,30:32.8071,31:32.0974,32:31.3412,33:30.5869,34:29.8343,35:29.0841,36:28.3362,37:27.5908,38:26.8482,39:26.1009,40:25.3728,41:24.6406,42:23.9126,43 : 23.184 , 44 :  22.4713 , 45:21.7592,46:21.0538,47:20.3555,48:19.6653,49:18.9841,50:18.3129,51:17.6525,52:17.005,53:16.371,54:15.7517,55:15.1478,56:14.5602,57:13.9888,58:13.434,59:12.8953,60:12.3719}
            rate=com_table2001[age_nb]
            
            return rate
        comm_rate=rate_anb(dor,dob)
        new_pensioner=Pensioner.objects.create(name=name, pay=pay, qs=qs, dob=dob, doa=doa, dor=dor, age=age, comm_rate=comm_rate)
        new_pensioner.save()
        pensioner=Pensioner.objects.all()
        return render(request, 'home.html', {'pensioner': pensioner})
    else:
        return render(request, 'add_new.html')

def home(request):
    pensioner=Pensioner.objects.all()
    return render(request, 'home.html', {'pensioner': pensioner}) 
   

    