from django.contrib import admin

from django.urls import path, include

from .views import login, signup, home, cart, checkout, orders, buynow, vlogin, vsignup, addproduct, showpro, payment


urlpatterns = [

    path('', home.Index.as_view(), name = 'home'),

    path('signup/', signup.Signup.as_view(), name = 'signup'),

    path('login/', login.Login.as_view(), name = 'login'),

    path('logout/',login.logout, name = 'logout'),

    path('cart/',cart.Cart.as_view(), name = 'cart'),

    path('check-out/', checkout.CheckOut.as_view(), name='checkout'),

    path('orders/', orders.OrderView.as_view(), name='orders'),

    path('buynow/', buynow.BuyNow.as_view(), name='buynow'),

    path('vsignup/', vsignup.Vsignup.as_view(), name='vsignup'),

    path('vlogin/', vlogin.Vlogin.as_view(), name='vlogin'),

    path('add_product/', addproduct.Addproduct.as_view(), name='add_product'),

    path('vlogout/',vlogin.vlogout, name = 'vlogout'),

    path('showpro/',showpro.Showpro.as_view(), name = 'showpro'),
    
    # path('payment/',payment.Payment.as_view(), name = 'payment'),
]

