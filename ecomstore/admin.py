from django.contrib import admin
from .models import *
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Orders)
admin.site.register(Off)
admin.site.register(Deal)
# Register your models here.
