from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
def index(request):
    products=Product.objects.all()
    deal=Deal.objects.all()
    off=Off.objects.all()
    context={'products':products,'deals':deal,'offs':off}
    return render(request,'static/index.html',context)

def signup(request):
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username,email,password)
        user.save()
    return render(request,"static/signup.html")
def loggin(request):
    if request.method=="POST":
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request,user)
        else:
            pass
    else:
        pass
    return render(request,"static/login.html")

@login_required
def checkout(request):
    orderitem=OrderItem.objects.all()
    order=Orders.objects.all()
    for i in range(len(orderitem)):
        order.total+=(orderitem[i].product.product_price)*(orderitem[i].quantity)
    order=Orders.objects.create(user=request.user,total=order.total)
    order.save()
    return render(request,"static/checkout.html",{'orderitems':orderitem})
def cart(request):
    order=OrderItem.objects.all()
    return render(request,"static/cart.html")
def addtocart(request):
    data=json.loads(request.body)
    productid=data['productid']
    action=data['action']
    print(productid)
    product=Product.objects.get(id=productid)
    orderitem,created=OrderItem.objects.get_or_create(product=product)
    print(data)
    if action=='add':
        orderitem.quantity+=1
    elif action=='remove':
        orderitem.quantity-=1
    orderitem.save()
    if orderitem.quantity<=0:
        orderitem.delete()
    return JsonResponse(productid,safe=True)
# Create your views here.
