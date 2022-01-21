
from django.shortcuts import redirect, render

from .models import *
from django.contrib import messages
from .models import con



def home(request):
    trending = product.objects.filter(trending=1)
   
    slide = mainslide.objects.all()
    b=ban.objects.all()
    context = {'trending':trending, 'slide':slide,'b':b}
    return render(request, 'Shop/index.html',context)

def collections(request):
    categor = category.objects.filter(status=0)
    context = {'category':categor}
    return render(request, 'Shop/collections.html', context)


def collectionsview(request, slug):
    if(category.objects.filter(slug=slug,status=0)):
        produc = product.objects.filter(category__slug=slug)
        categor=category.objects.filter(slug=slug).first
        context = {'produc':produc, 'category':categor}
        return render(request,'Shop/products/index.html',context)
    else:
        messages.warning(request,"No search category is found")
        return redirect("collections")
        

def productview(request, cate_slug , prod_slug):
    if(category.objects.filter(slug=cate_slug,status=0)):
         if(product.objects.filter(slug=prod_slug,status=0)):
             products= product.objects.filter(slug=prod_slug,status=0).first
             context={"products":products}
             
            
        
         else:
             messages.error(request, "No such product found")
             return redirect("collections")
        
        
    else:
        messages.error(request, "No such category found")
        return redirect("collections")
    
    return render(request,"Shop/products/view.html",context)


def contactus(request):
    if request.method=="POST":
        co=con()
        name=request.POST['name']
        email=request.POST['EMAIL']
        message=request.POST['message']
        co.name=name
        co.email=email
        co.message=message
        co.save()
        messages.success(request,"Submission Successful")
        return redirect("/")
    
    
    
    return render(request,'Shop/inc/contactus.html')



