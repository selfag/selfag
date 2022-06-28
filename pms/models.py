from pyexpat import model
from django.db import models

# Create your models here.
class Pensioner(models.Model):
    name=models.CharField(max_length=200)
    fname=models.CharField(max_length=200, null=True)
    fpname=models.CharField(max_length=200, null=True)
    pay=models.IntegerField(null=True)
    qs=models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=200, null=True)
    comm_rate=models.DecimalField(decimal_places=4, max_digits=8, null=True)
    dob=models.CharField(max_length=20,null=True)
    dobf=models.CharField(max_length=20,null=True)
    doa=models.CharField(max_length=20,null=True)
    dor=models.CharField(max_length=20,null=True)
    dod=models.CharField(max_length=20,null=True)
    gp=models.FloatField(null=True)
    np=models.FloatField(null=True)
    comm_amount=models.FloatField(null=True)
    inc03=models.FloatField(null=True)
    inc04=models.FloatField(null=True)
    inc05=models.FloatField(null=True)
    inc06=models.FloatField(null=True)
    inc07=models.FloatField(null=True)
    inc08=models.FloatField(null=True)
    inc09=models.FloatField(null=True)
    inc10=models.FloatField(null=True)
    inc11=models.FloatField(null=True)
    inc12=models.FloatField(null=True)
    inc13=models.FloatField(null=True)
    inc14=models.FloatField(null=True)
    inc15=models.FloatField(null=True)
    inc16=models.FloatField(null=True)
    inc17=models.FloatField(null=True)
    inc18=models.FloatField(null=True)
    inc19=models.FloatField(null=True)
    inc21=models.FloatField(null=True)
    inc22=models.FloatField(null=True)
    incm=models.FloatField(null=True)
    cp=models.FloatField(null=True)
    ma2010=models.FloatField(null=True)
    ma2015=models.FloatField(null=True)
    tp=models.FloatField(null=True)
    ppo=models.CharField(max_length=9, null=True, unique=True)
    bps=models.IntegerField(null=True)
    rbs=models.IntegerField(null=True)
    cnic=models.CharField(max_length=13, null=True, unique=True)
    qpay=models.IntegerField(null=True)
    ppay=models.IntegerField(null=True)
    spay=models.IntegerField(null=True)
    ui=models.IntegerField(null=True)
    opay=models.IntegerField(null=True)
    cat=models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200, null=True)
    designation=models.CharField(max_length=50, null=True)
    restd=models.CharField(max_length=20,null=True)
    

    
    def __str__(self):
        return self.name
    


class Bank(models.Model):
    pensioner=models.ForeignKey(Pensioner, on_delete=models.CASCADE)
    bname=models.CharField(max_length=10)
    bb=models.CharField(max_length=20)
    acctno=models.CharField(max_length=20)

    def __str__(self):
        return self.acctno



    
