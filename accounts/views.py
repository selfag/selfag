from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
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
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email already registered")
            user=User.objects.create_user(username=username,first_name=first_name, last_name=last_name, password=password1,email=email)
            user.save()
            return redirect("/")
        else:
            print("password in not matching")
            return render(request, 'register.html')
    return render(request, 'register.html')


    