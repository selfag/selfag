from posixpath import split
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Pensioner
from datetime import datetime, date
from django.db.models import Sum
from django.contrib.auth.decorators import login_required





# Create your views here.

def welcome(request):
    pensioner=Pensioner.objects.count()
    netpension=Pensioner.objects.all().aggregate(tp=Sum('np'))
    ma=Pensioner.objects.all().aggregate(tma=Sum('ma2010'))
    ma2=Pensioner.objects.all().aggregate(tma2=Sum('ma2015'))
    lts=Pensioner.objects.latest('id')
    oldage=Pensioner.objects.filter(tp__lte=50000).count()
    return render(request, 'welcome.html',{'pensioner':pensioner, 'netpension': netpension,'lts':lts, 'oldage':oldage, 'ma':ma, 'ma2':ma2})
def add_new(request):
    if request.method=="POST":
        name=request.POST['name']
        pay=request.POST['pay']
        d1,m1,y1= [int(x) for x in request.POST['dob'].split('-')]
        d2,m2,y2= [int(x) for x in request.POST['doa'].split('-')]
        d3,m3,y3= [int(x) for x in request.POST['dor'].split('-')]
        
        db=date(y1,m1,d1)
        dob=db.strftime("%d-%m-%Y")
        da=date(y2,m2,d2)
        doa=da.strftime("%d-%m-%Y")
        dr=date(y3,m3,d3)
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
    pensioner=Pensioner.objects.all().order_by('id')
    return render(request, 'home.html', {'pensioner': pensioner}) 

def revise(request):
    if request.method=="POST":
        id=request.POST['id']
        pensioner=Pensioner.objects.filter(id=id)
        return render(request, 'revise.html', {'pensioner': pensioner})
    else:
        return render(request, 'revise.html')

def calculate(request):
    if request.method=="POST":
        id=request.POST['id']
        pensioner=Pensioner.objects.filter(id=id)
        return render(request, 'calculate.html', {'pensioner': pensioner})
    else:
        return render(request, 'calculate.html')


def update(request, id):
    pensioner=Pensioner.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        pay=request.POST['pay']
        d1,m1,y1= [int(x) for x in request.POST['dob'].split('-')]
        d2,m2,y2= [int(x) for x in request.POST['doa'].split('-')]
        d3,m3,y3= [int(x) for x in request.POST['dor'].split('-')]
        
        db=date(y1,m1,d1)
        dob=db.strftime("%d-%m-%Y")
        da=date(y2,m2,d2)
        doa=da.strftime("%d-%m-%Y")
        dr=date(y3,m3,d3)
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
        
        db=date(y1,m1,d1)
        dob=db.strftime("%d-%m-%Y")
        da=date(y2,m2,d2)
        doa=da.strftime("%d-%m-%Y")
        dr=date(y3,m3,d3)
        dor=dr.strftime("%d-%m-%Y")
        red=date(y3,m3,d3)
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
        datediff(d2,m2,y2,d3,m3,y3)
        qs=f"{years} Y-{months} M-{days} D"
        
        if months>=6:
            nqs=years+1
        else:
            nqs=years
        if nqs>30:
            nqs=30
        gp=round(int(pay)*nqs/30*0.7,2)
        npo=round(gp*0.65,2)
        np=npo
        cp=round(gp*0.35)
        comm_amount=round(cp*12*comm_rate,2)
        d2002=date(2002,7,1)
        d2005=date(2005,7,1)
        d2007=date(2007,7,1)
        d2008=date(2008,7,1)
        d2009=date(2009,7,1)
        d2011=date(2011,7,1)
        d2015=date(2015,7,1)
        d2016=date(2016,7,1)
        d2017=date(2017,7,1)
        ma2010=round(np*0.25)
        ma2015=round(ma2010*0.25)
        
        inc=[]
        inc03=0
        inc04=0 
        inc05=0
        inc06=0
        inc07=0
        inc08=0
        inc09=0
        inc10=0
        inc11=0
        inc12=0
        inc13=0
        inc14=0
        inc15=0
        inc16=0
        inc17=0
        inc18=0
        inc19=0
        inc21=0
        if dr<d2005:
            inc03=round(np*0.15)
            np=np+inc03
            if np<300:
                np=300
                inc03=np-inc03
            if dr>date(2003,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2003,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc03,np])

        if dr<d2005:
            inc04=round(np*0.08)
            np=np+inc04
            if np<300:
                np=300
                inc04=np-inc04
            if dr>date(2004,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2004,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc04,np])
            

        if dr<d2011:
            inc05=round(np*0.10)
            np=np+inc05
            if np<300:
                np=300
                inc05=np-inc05
            if dr>date(2005,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2005,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc05,np])
        if dr<d2011:
            inc06=round(np*0.15)
            np=np+inc06
            if np<300:
                np=300
                inc06=np-inc06
            if dr>date(2006,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2006,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc06,np])
            
        if dr<d2007:
            inc07=round(np*0.15)
            np=np+inc07
            if np<300:
                np=300
                inc07=np-inc07
            if dr>date(2007,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2007,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc07,np])

        if dr<d2008:
            inc08=round(np*0.20)
            np=np+inc08
            if np<2000:
                np=2000
                inc08=np-inc08
            if dr>date(2008,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2008,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc08,np])
        if dr<d2009:
            inc09=round(np*0.15)
            np=np+inc09
            if np<2000:
                np=2000
                inc09=np-inc09
            if dr>date(2009,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2009,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc09,np])
        if dr<d2017:
            inc10=round(np*0.15)
            np=np+inc10
            ma2010=round(np*0.25)
            ma2015=round(ma2010*0.25)
            if np<3000:
                np=3000
                inc10=np-inc10
            if dr>date(2010,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2010,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc10,np])
        if dr<d2002:
            inc11=round(np*0.20)
            np=np+inc11
            if np<3000:
                np=3000
                inc11=np-inc11
            if dr>date(2011,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2011,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc11,np])
        elif dr>=d2002:
            inc11=round(np*0.15)
            np=np+inc11
            if np<3000:
                np=3000
                inc11=np-inc11
            if dr>date(2011,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2011,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc11,np])
        if dr<d2015:
            inc12=round(np*0.20)
            np=np+inc12
            if np<3000:
                np=3000
                inc12=np-inc12
            if dr>date(2012,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2012,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc12,np])
        if dr<d2016:
            inc13=(np*0.10)
            np=np+inc13
            if dr>date(2013,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2013,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc13,np])
        if dr<d2016:
            inc14=round(np*0.10)
            np=np+inc14
            if dr>date(2014,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2014,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc14,np])
        if dr:
            inc15=round(np*0.075)
            np=np+inc15
            if dr>date(2015,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2015,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc15,np])

        if dr:
            inc16=round(np*0.10)
            np=np+inc16
            if dr>date(2016,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2016,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc16,np])

        if dr:
            inc17=round(np*0.10)
            np=np+inc17
            if dr>date(2017,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2017,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc17,np])

        if dr:
            inc18=round(np*0.10)
            np=np+inc18
            if dr>date(2018,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2018,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc18,np])

        if dr:
            inc19=round(np*0.10)
            np=np+inc19
            if dr>date(2019,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2019,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc19,np])

        if dr:
            inc21=round(np*0.10)
            np=np+inc21
            if dr>date(2021,7,1):
                wef=dr.strftime("%d-%m-%Y")
            else:
                wef=date(2021,7,1).strftime("%d-%m-%Y")
            inc.append([wef,inc21,np])
            tp=np+ma2010+ma2015
       
        pensioner=Pensioner.objects.filter(id=id).update(name=name, pay=pay, dob=dob, doa=doa, dor=dor, age=age,qs=qs, comm_rate=comm_rate, gp=gp, np=npo, comm_amount=comm_amount,inc03=inc03, inc04=inc04, inc05=inc05, inc06=inc06, inc07=inc07, inc08=inc08, inc09=inc09, inc10=inc10, inc11=inc11, inc12=inc12, inc13=inc13, inc14=inc14, inc15=inc15,inc16=inc16,inc17=inc17,inc18=inc18,inc19=inc19,inc21=inc21, ma2010=ma2010, ma2015=ma2015, tp=tp)
        
        return redirect("/candr")
    
def candr(request):
    if request.method=="POST":
        global d
        d=request.POST['number']
        pensioner=Pensioner.objects.filter(id=d)
        return render(request, 'candr.html', {'pensioner':pensioner})
    else:
        pensioner=Pensioner.objects.all()
        return render(request, 'candr.html')


        

   

    