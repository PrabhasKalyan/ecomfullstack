from django.urls import path
from . import views
urlpatterns=[
    path('store/',views.index,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('addtocart/',views.addtocart,name="addtocart"),
    path('signup/',views.signup,name="addtocart"),
    path('login/',views.login,name="addtocart"),
]