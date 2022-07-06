from django.urls import path
from .import views

app_name="pms"

urlpatterns=[
    path('', views.welcome, name="welcome"),
    path('add_new', views.add_new, name="add_new"),
    path('home', views.home, name="home"),
    path('revise', views.revise, name="revise"),
    path('update/<int:id>', views.update, name="update"),
    path('calculate', views.calculate, name="calculate"),
    path('calculator/<int:id>', views.calculator, name="calculator"),
    path('candr', views.candr, name="candr"),
    path('simple_calculator', views.listcontent, name="simple_calculator")
]
