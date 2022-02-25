from django.urls import path
from .import views

app_name="pms"

urlpatterns=[
    path('', views.welcome),
    path('add_new', views.add_new),
    path('home', views.home),
    path('revise/<int:id>', views.revise),
    path('revise/update/<int:id>', views.update ),
]
