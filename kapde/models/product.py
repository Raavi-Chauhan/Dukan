from django.db import models
from .catagory import Catagory
from .vendor import Vendor

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=30)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/products/')
    sale = models.IntegerField(default=0)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    
    @staticmethod
    def get_all_products_by_catagoryid(catagory_id):
        if catagory_id:
            return Product.objects.filter(catagory = catagory_id)

        else:
            return Product.get_all_products()

    
    @staticmethod
    def get_product_by_search(search):
        srch = " " + search
        pro = Product.objects.filter(name__contains = srch)
        return pro

    # @staticmethod
    # def remove_product_by_id(ides):
    #     return product.objects.filter(id__in=ides)