from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
           
        else:
            messages.info(request, "creditial are invalid")
            return render(request, 'login.html')
    return render(request, 'login.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already Taken")
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email already registered")
                return render(request, 'register.html')
            user=User.objects.create_user(username=username,first_name=first_name, last_name=last_name, password=password1,email=email)
            user.save()
            return render(request, "login.html")
        else:
            messages.info(request, "Password not matching")
            return render(request, 'register.html')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')