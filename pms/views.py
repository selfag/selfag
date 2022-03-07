from posixpath import split
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Pensioner
import datetime
from django.views.generic import TemplateView





# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def add_new(request):
    if request.method=="POST":
        name=request.POST['name']
        pay=request.POST['pay']
        d1,m1,y1= [int(x) for x in request.POST['dob'].split('-')]
        d2,m2,y2= [int(x) for x in request.POST['doa'].split('-')]
        d3,m3,y3= [int(x) for x in request.POST['dor'].split('-')]
        
        db=datetime.datetime(y1,m1,d1)
        dob=db.strftime("%d-%m-%Y")
        da=datetime.datetime(y2,m2,d2)
        doa=da.strftime("%d-%m-%Y")
        dr=datetime.datetime(y3,m3,d3)
        dor=dr.strftime("%d-%m-%Y")
        def datediff(d1,m1,y1,d2,m2,y2):
            global years, months, days
            if y2>=y1:
                if d2>=d1 and m2>=m1:
                    days=d2-d1
                    months=m2-m1
                    years=y2-y1
                    #print(f"{years} years {months} months {days} days")
                if d2>=d1 and m2<m1:
                    days=d2-d1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    months=m2-m1
                    years=y2-y1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [1,3,5,7,8,10,12]:
                    d2=d2+31
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [4,6,9,11]:
                    d2=d2+30
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [2] and y2%4==0:
                    d2=d2+29
                    if d2<d1:
                        d2=d2+31
                        m2=m2-1
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [2] and y2%4!=0:
                    d2=d2+28
                    if d2<d1:
                        d2=d2+31
                        m2=m2-1
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
            return years, months, days
        a=datediff(d1,m1,y1,d3,m3,y3)
        age=f"{years}M-{months}M-{days}D"
        age_nb=years+1
        if age_nb>60:
            age_nb=60
        com_table2001 ={20:40.5043, 21:39.7341, 22:38.9653,23:38.1974,24:37.4307,25:36.6651,26:35.9006,27:35.1372,28:34.3750,29:33.6143,30:32.8071,31:32.0974,32:31.3412,33:30.5869,34:29.8343,35:29.0841,36:28.3362,37:27.5908,38:26.8482,39:26.1009,40:25.3728,41:24.6406,42:23.9126,43 : 23.184 , 44 :  22.4713 , 45:21.7592,46:21.0538,47:20.3555,48:19.6653,49:18.9841,50:18.3129,51:17.6525,52:17.005,53:16.371,54:15.7517,55:15.1478,56:14.5602,57:13.9888,58:13.434,59:12.8953,60:12.3719}
        comm_rate=com_table2001[age_nb]
        s=datediff(d2,m2,y2,d3,m3,y3)
        qs=f"{years}M-{months}M-{days}D"

        new_pensioner=Pensioner.objects.create(name=name, pay=pay, dob=dob, doa=doa, dor=dor, age=age,qs=qs, comm_rate=comm_rate)
        new_pensioner.save()
        pensioner=Pensioner.objects.all()
        return redirect("/home")
    else:
        return render(request, 'add_new.html')

def home(request):
    pensioner=Pensioner.objects.all()
    return render(request, 'home.html', {'pensioner': pensioner}) 

def revise(request, id):
    pensioner=Pensioner.objects.get(id=id)
    return render(request, 'revise.html', {'pensioner': pensioner})

def calculate(request, id):
    pensioner=Pensioner.objects.get(id=id)
    return render(request, 'calculate.html', {'pensioner': pensioner})


def update(request, id):
    pensioner=Pensioner.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        pay=request.POST['pay']
        d1,m1,y1= [int(x) for x in request.POST['dob'].split('-')]
        d2,m2,y2= [int(x) for x in request.POST['doa'].split('-')]
        d3,m3,y3= [int(x) for x in request.POST['dor'].split('-')]
        
        db=datetime.datetime(y1,m1,d1)
        dob=db.strftime("%d-%m-%Y")
        da=datetime.datetime(y2,m2,d2)
        doa=da.strftime("%d-%m-%Y")
        dr=datetime.datetime(y3,m3,d3)
        dor=dr.strftime("%d-%m-%Y")
        def datediff(d1,m1,y1,d2,m2,y2):
            global years, months, days
            if y2>=y1:
                if d2>=d1 and m2>=m1:
                    days=d2-d1
                    months=m2-m1
                    years=y2-y1
                    #print(f"{years} years {months} months {days} days")
                if d2>=d1 and m2<m1:
                    days=d2-d1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    months=m2-m1
                    years=y2-y1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [1,3,5,7,8,10,12]:
                    d2=d2+31
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [4,6,9,11]:
                    d2=d2+30
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [2] and y2%4==0:
                    d2=d2+29
                    if d2<d1:
                        d2=d2+31
                        m2=m2-1
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [2] and y2%4!=0:
                    d2=d2+28
                    if d2<d1:
                        d2=d2+31
                        m2=m2-1
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
            return years, months, days
        a=datediff(d1,m1,y1,d3,m3,y3)
        age=f"{years} Y-{months} M-{days} D"
        age_nb=years+1
        if age_nb>60:
            age_nb=60
        print(age_nb)
        com_table2001 ={20:40.5043, 21:39.7341, 22:38.9653,23:38.1974,24:37.4307,25:36.6651,26:35.9006,27:35.1372,28:34.3750,29:33.6143,30:32.8071,31:32.0974,32:31.3412,33:30.5869,34:29.8343,35:29.0841,36:28.3362,37:27.5908,38:26.8482,39:26.1009,40:25.3728,41:24.6406,42:23.9126,43 : 23.184 , 44 :  22.4713 , 45:21.7592,46:21.0538,47:20.3555,48:19.6653,49:18.9841,50:18.3129,51:17.6525,52:17.005,53:16.371,54:15.7517,55:15.1478,56:14.5602,57:13.9888,58:13.434,59:12.8953,60:12.3719}
        comm_rate=com_table2001[age_nb]
        s=datediff(d2,m2,y2,d3,m3,y3)
        qs=f"{years} Y-{months} M-{days} D"

        Pensioner.objects.filter(id=id).update(name=name, pay=pay, dob=dob, doa=doa, dor=dor, age=age,qs=qs, comm_rate=comm_rate)
        
        return redirect("/home")
    else:
        return render(request, 'welcome.html')
    
def calculator(request, id):
    if request.method=="POST":
        name=request.POST['name']
        pay=request.POST['pay']
        d1,m1,y1= [int(x) for x in request.POST['dob'].split('-')]
        d2,m2,y2= [int(x) for x in request.POST['doa'].split('-')]
        d3,m3,y3= [int(x) for x in request.POST['dor'].split('-')]
        
        db=datetime.datetime(y1,m1,d1)
        dob=db.strftime("%d-%m-%Y")
        da=datetime.datetime(y2,m2,d2)
        doa=da.strftime("%d-%m-%Y")
        dr=datetime.datetime(y3,m3,d3)
        dor=dr.strftime("%d-%m-%Y")
        def datediff(d1,m1,y1,d2,m2,y2):
            global years, months, days
            if y2>=y1:
                if d2>=d1 and m2>=m1:
                    days=d2-d1
                    months=m2-m1
                    years=y2-y1
                    #print(f"{years} years {months} months {days} days")
                if d2>=d1 and m2<m1:
                    days=d2-d1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    months=m2-m1
                    years=y2-y1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [1,3,5,7,8,10,12]:
                    d2=d2+31
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [4,6,9,11]:
                    d2=d2+30
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [2] and y2%4==0:
                    d2=d2+29
                    if d2<d1:
                        d2=d2+31
                        m2=m2-1
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
                    #print(f"{years} years {months} months {days} days")
                elif d2<d1 and m2 in [2] and y2%4!=0:
                    d2=d2+28
                    if d2<d1:
                        d2=d2+31
                        m2=m2-1
                    m2=m2-1
                    if m2<m1:
                        m2=m2+12
                        y2=y2-1
                    years=y2-y1
                    months=m2-m1
                    days=d2-d1
            return years, months, days
        a=datediff(d1,m1,y1,d3,m3,y3)
        age=f"{years} Y-{months} M-{days} D"
        age_nb=years+1
        if age_nb>60:
            age_nb=60
        print(age_nb)
        com_table2001 ={20:40.5043, 21:39.7341, 22:38.9653,23:38.1974,24:37.4307,25:36.6651,26:35.9006,27:35.1372,28:34.3750,29:33.6143,30:32.8071,31:32.0974,32:31.3412,33:30.5869,34:29.8343,35:29.0841,36:28.3362,37:27.5908,38:26.8482,39:26.1009,40:25.3728,41:24.6406,42:23.9126,43 : 23.184 , 44 :  22.4713 , 45:21.7592,46:21.0538,47:20.3555,48:19.6653,49:18.9841,50:18.3129,51:17.6525,52:17.005,53:16.371,54:15.7517,55:15.1478,56:14.5602,57:13.9888,58:13.434,59:12.8953,60:12.3719}
        comm_rate=com_table2001[age_nb]
        s=datediff(d2,m2,y2,d3,m3,y3)
        qs=f"{years} Y-{months} M-{days} D"
        
        if months>=6:
            nqs=years+1
        else:
            nqs=years
        gp=round(int(pay)*nqs/30*0.7,2)
        np=round(gp*0.65,2)
        cp=round(gp*0.35)
        comm_amount=round(cp*12*comm_rate,2)

        Pensioner.objects.filter(id=id).update(name=name, pay=pay, dob=dob, doa=doa, dor=dor, age=age,qs=qs, comm_rate=comm_rate, gp=gp, np=np, comm_amount=comm_amount)
        context=Pensioner.objects.filter(id=id)
    return redirect("/candr")
    
def candr(request):
    if request.method=="POST":
        global d
        d=request.POST['number']
        pensioner=Pensioner.objects.filter(id=d)
        return render(request, 'candr.html', {'pensioner':pensioner})
    else:
        return render(request, 'candr.html')
        

   

    