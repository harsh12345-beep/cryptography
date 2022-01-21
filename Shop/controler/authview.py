from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages

from Shop.forms import registerform


def register(request):
    form = registerform()
    if request.method=="POST":
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully")
            return redirect("login")
    context = {'forms':form}
    return render(request,"Shop/ACCOUNT/register.html",context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already loggedin')
        return redirect("Index")
    else:
        if request.method == "POST":
            name = request.POST.get('name')
            pwd = request.POST.get('pas')
            
            user = authenticate(request, username=name,password=pwd)
            
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("Index")
            else:
                messages.error(request,"Invlaid username or password")
                return redirect("login")
            
        return render(request,"SHop/ACCOUNT/login.html") 
    

def logoutpage(request):
    if request.user.is_authenticated:
        
        logout(request)
        messages.success(request,"Logged out successfully")
    return redirect("Index")

