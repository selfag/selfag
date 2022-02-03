from django.db import models

# Create your models here.
class Pensioner(models.Model):
    name=models.CharField(max_length=200)
    pay=models.IntegerField()
    qs=models.IntegerField()
    age=models.CharField(max_length=200, null=True)
    comm_rate=models.DecimalField(decimal_places=4, max_digits=8, null=True)
    dob=models.DateField(null=True)
    doa=models.DateField(null=True)
    dor=models.DateField(null=True)
    
    def __str__(self):
        return self.name