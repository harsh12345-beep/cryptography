from django.contrib import admin
from django.urls import path,include
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth import views as auth_views
from Shop.controler import authview,cart
urlpatterns = [
    path('',views.home,name='Index'),
    path('collections',views.collections,name="collections"),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),  
    path('contactus',views.contactus,name="contactus"),
    path("register",authview.register , name="register"),
    path("loginpage",authview.loginpage,name="login"),
    path("logoutpage",authview.logoutpage,name="logout"),
    path('addtocart',cart.addtocart,name="addtocart"),
    path("cart",cart.viewcart,name="cart"),
    path('cartupdate',cart.update,name="update"),
    path("delete-cart-item", cart.delete, name="delete"),
    path("checkout", cart.checkout, name="checkout"),
    path("placeorder", cart.placeorder, name="placeorder"),
    path("myorders", cart.myorders, name="myorders"),
    path("orderview/<str:t_no>", cart.orderview, name="orderview"),
    path("walletindex", cart.walletindex, name="walletindex"),

    
    path('social-auth/', include('social_django.urls', namespace="social")),
    
    
   
 
  

]

