from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=256)
    price=models.FloatField()
    image=models.ImageField(null=True,upload_to='static/images')
    def __str__(self):
        return self.name
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total
    def __str__(self):
        return self.product.name
class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total=models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
class Deal(models.Model):
    prods=models.ForeignKey(Product,on_delete=models.CASCADE)
class Off(models.Model):
    offs=models.ForeignKey(Product,on_delete=models.CASCADE)
    
class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200,null=False)
    city=models.CharField(max_length=200,null=False)
    state=models.CharField(max_length=200,null=False)
    zipcode=models.CharField(max_length=200,null=False)
    def __str__(self):
        return self.address

# Create your models here.
