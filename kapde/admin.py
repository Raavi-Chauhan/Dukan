from django.contrib import admin
from .models.product import Product
from .models.catagory import Catagory
from .models.customer import Customer
from .models.orders import Order
from .models.vendor import Vendor
from .models.company import Company

# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'vendor', 'price', 'catagory']

class AdminCatagory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone']

class AdminCompany(admin.ModelAdmin):
    list_display = ['name']

class AdminVendor(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

admin.site.register(Product, AdminProduct)
admin.site.register(Catagory, AdminCatagory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order)
admin.site.register(Company,AdminCompany)
admin.site.register(Vendor, AdminVendor)