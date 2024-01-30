from django.db import models
from .company import Company

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name