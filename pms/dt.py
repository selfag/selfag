from datetime import date
dor=date(2015,5,12)
d2002=date(2002,7,1)
d2005=date(2005,7,1)
d2007=date(2007,7,1)
d2008=date(2008,7,1)
d2009=date(2009,7,1)
d2011=date(2011,7,1)
d2015=date(2015,7,1)
d2016=date(2016,7,1)
d2017=date(2017,7,1)
inc={}
if dor<d2005:
    inc['inc03']=0.15

if dor<d2005:
    inc['inc04']=0.08

if dor<d2011:
    inc['inc05']=0.10

if dor<d2011:
    inc['inc06']=0.15

if dor<d2007:
    inc['inc07']=0.15

if dor<d2008:
    inc['inc08']=0.20

if dor<d2009:
    inc['inc09']=0.15

if dor<d2017:
    inc['inc10']=0.15

if dor<d2002:
    inc['inc11']=0.20
elif dor>=d2002:
    inc['inc11']=0.15
if dor<d2015:
    inc['inc12']=0.20

if dor<d2016:
    inc['inc13']=0.10
if dor<d2016:
    inc['inc14']=0.10
if dor:
    inc['inc15']=0.075

if dor:
    inc['inc16']=0.10

if dor:
    inc['inc17']=0.10

if dor:
    inc['inc18']=0.10

if dor:
    inc['inc19']=0.10

if dor:
    inc['inc21']=0.10

print(inc) 
np=15925
if 'inc10' not in inc:
        ma2010=np*0.25
        ma2015=ma2010*0.25
        print(ma2010, ma2015)

    
for i, j in inc.items():
    ic=round(np*j,2)
    np=round(np+ic,2)
    
    if np<300 and i in ['inc03','inc04','inc05','inc06','inc07']:
        np=300
        ic=f"{np-ic} Minimum Pension"
    elif np<2000 and i in ['inc08','inc09']:
        np=2000
        ic=f"{np-ic} Minimum Pension"
    elif np<3000 and i in ['inc10','inc11','inc12']:
        np=3000
       
        ic=f"{np-ic} Minimum Pension"
    elif np<5000 and i in ['inc13']:
        np=5000
        ic=f"{np-ic} Minimum Pension"
    elif np<6000 and i in ['inc14','inc15','inc16','inc17']:
        np=6000
        ic=f"{np-ic} Minimum Pension"
   
    elif np<10000 and i in ['inc18','inc19','inc21']:
        np=10000
        ic=f"{np-ic} Minimum Pension"
    
    print(i,ic,np)
 

