from django.db import models

# Create your models here.
class Pensioner(models.Model):
    name=models.CharField(max_length=200)
    pay=models.IntegerField(null=True)
    qs=models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=200, null=True)
    comm_rate=models.DecimalField(decimal_places=4, max_digits=8, null=True)
    dob=models.CharField(max_length=20,null=True)
    doa=models.CharField(max_length=20,null=True)
    dor=models.CharField(max_length=20,null=True)
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
    ma2010=models.FloatField(null=True)
    ma2015=models.FloatField(null=True)
    tp=models.FloatField(null=True)

    
    def __str__(self):
        return self.name
    
class Increase(models.Model):
    name=models.CharField(max_length=20, unique=True)
    startdate=models.DateField()
    enddate=models.DateField()
    rate=models.FloatField()

    def __str__(self):
        return self.name



    
