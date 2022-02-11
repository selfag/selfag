from datetime import date
from pickle import GET
<form>
<input type="date" name="dob">
a= GET["dob"]
y=a.month
y=y+3
b=date(2000,5,15)
c=a-b
print(c)
print("year",y)