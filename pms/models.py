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
    
    def __str__(self):
        return self.name