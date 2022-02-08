from datetime import date
a=date.today()
y=a.month
y=y+3
b=date(2000,5,15)
c=a-b
print(c)
print("year",y)