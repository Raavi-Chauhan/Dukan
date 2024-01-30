from django.shortcuts import render, redirect
from django.views import View
from kapde.models.product import Product
from kapde.models.vendor import Vendor
from kapde.models.catagory import Catagory


class Addproduct(View):
    def get(self, request):
        
        try:
            if request.session['vendor']:
                a = request.session['vendor']
                info = {
                    'catagories' :Catagory.objects.all(),
                    'name' : Vendor.objects.get(id=a).name
                    }
                    
                return render(request, 'add_product.html', info)

        except:
            return redirect('vlogin')


    def post(self, request):
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        idocg = int(request.POST.get('catagory'))
        img = request.POST.get('pimage')
        image =  'uploads/products/'+img

        idov = request.session['vendor']

        try:
            vendor = Vendor.objects.get(id=idov)
        except:
            pass

        try:
            catagory = Catagory.objects.get(id=idocg)
        except:
            pass

        value = {
            'name': name,
            'price': price
        }

        product = Product(name=name, price=price, stock=stock, catagory=catagory, vendor=vendor, image=image)
        error_message = None

        if (len(name)<1):
            error_message = "Enter a valid name!"

        if (int(price) < 0):
            error_message = "Enter valid amount!"

        if (int(stock) <= 0):
            error_message = "Stock should be available!"

        if Product.objects.filter(name=name):
            error_message = "Product name already exist!"

        if not error_message:
            product.save()
            return redirect('home')

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'add_product.html', data)