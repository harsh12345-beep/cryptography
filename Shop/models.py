from email import message
from email.headerregistry import Address
from email.mime import text
from http.client import PAYMENT_REQUIRED
from operator import mod
from pyexpat import model
from sre_parse import State
from statistics import mode, quantiles
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models
import datetime
import os
from django.contrib.auth.models import User
from django.db.models.base import Model
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%M%D%H:%M%S')    
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/', filename)

class category(models.Model):
    slug = models.CharField (max_length=150,null=False,blank=False)
    name = models.CharField (max_length=150,null=False,blank=False)
    image = models.ImageField( upload_to=get_file_path, null=True, blank=True)
    Description = models.TextField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=trending")
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords =  models.CharField(max_length=150,null=False,blank=False)
    meta_description =  models.TextField(max_length=500,null=False,blank=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
         
    
    
class product(models.Model):
    
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    slug = models.CharField (max_length=150,null=False,blank=False)
    name = models.CharField (max_length=150,null=False,blank=False)
    product_image = models.ImageField( upload_to=get_file_path, null=False, blank=False)
    small_Description = models.CharField(max_length=300,null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    Description = models.TextField(max_length=500,null=False,blank=False)
    orignal_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=trending")
    tag = models.CharField(max_length=300,null=False,blank=False)
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords =  models.CharField(max_length=150,null=False,blank=False)
    meta_description =  models.TextField(max_length=500,null=False,blank=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class con(models.Model):
    name=models.CharField(max_length=100,null=False)
    email=models.EmailField(max_length=30,null=False)
    message=models.TextField(max_length=1000,null=False)
        
    def __str__(self):
        return self.name
        


class MAINPAGEPRODUCTS(models.Model):
    
    SSlug = models.CharField (max_length=150,null=False,blank=False)
    NName = models.CharField (max_length=150,null=False,blank=False)
    PProduct_image = models.ImageField( upload_to=get_file_path, null=False, blank=False)
    SSmall_Description = models.CharField(max_length=300,null=False,blank=False)
    QQuantity = models.IntegerField(null=False,blank=False)
    DDescription = models.TextField(max_length=500,null=False,blank=False)
    OOrignal_price = models.FloatField(null=False,blank=False)
    SSelling_price = models.FloatField(null=False,blank=False)
    SStatus = models.BooleanField(default=False,help_text="0=default, 1=hidden")
    TTrending = models.BooleanField(default=False,help_text="0=default, 1=trending")
    TTag = models.CharField(max_length=300,null=False,blank=False)
    MMeta_title = models.CharField(max_length=150,null=False,blank=False)
    MMeta_keywords =  models.CharField(max_length=150,null=False,blank=False)
    MMeta_description =  models.TextField(max_length=500,null=False,blank=False) 
    CCreated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.NName
    
    

        

    
class mainslide(models.Model):
    SSSlug = models.CharField (max_length=150,null=False,blank=False)
    NNName = models.CharField (max_length=150,null=False,blank=False)
    PPProduct_image = models.ImageField( upload_to=get_file_path, null=False, blank=False)
    SSSmall_Description = models.CharField(max_length=300,null=False,blank=False)
    QQQuantity = models.IntegerField(null=False,blank=False)
    DDDescription = models.TextField(max_length=500,null=False,blank=False)
    OOOrignal_price = models.FloatField(null=False,blank=False)
    SSSelling_price = models.FloatField(null=False,blank=False)
    SSStatus = models.BooleanField(default=False,help_text="0=default, 1=hidden")
    
    
    def __str__(self):
        return self.NNName
    
class ban(models.Model):
       
    PPPProduct_image = models.ImageField( upload_to=get_file_path, null=False, blank=False)
    NNNName = models.CharField (max_length=150,null=False,blank=False)
    
    
    def __str__(self):
        return self.NNNName
    
class art(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
class order(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=150,null=False)
    lname=models.CharField(max_length=150,null=False)
    email=models.EmailField(max_length=150,null=False)
    phone=models.CharField(max_length=150,null=False)
    Address=models.TextField(null=False) 
    city=models.CharField(max_length=150,null=False) 
    State=models.CharField(max_length=150,null=False) 
    country=models.CharField(max_length=150,null=False) 
    pin=models.CharField(max_length=150,null=False) 
    adhar=models.CharField(max_length=150,null=False) 
    total_price = models.FloatField(null=False)
    payment_id = models.CharField(max_length=400,null=False)
    orderstatus =(
        ('pending','pending'),
        ('Out for shipping','Out for shipping'),
        ('delivered','delivered')
        
    )
    status = models.CharField(max_length=150,choices=orderstatus, default='pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150,null=False)
    created_on = models.DateTimeField( auto_now_add=True)
    updated_on =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)
    
class OrderItem(models.Model):
    orde = models.ForeignKey(order,on_delete=models.CASCADE)
    Product = models.ForeignKey(product, on_delete=models.CASCADE) 
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    
    def __str__(self):
        return '{}  {}'.format(self.order.id, self.order.tracking_no)  
    
class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(MAINPAGEPRODUCTS, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    