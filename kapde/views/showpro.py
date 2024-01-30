from django.shortcuts import render, redirect
from kapde.models.product import Product
from kapde.models.vendor import Vendor
from django.views import View

class Showpro(View):
    def get(self, request):
        try:
            if request.session['vendor']:

                ids = int(request.session['vendor'])
                name = Vendor.objects.get(id=ids).name
                products = list(Product.objects.filter(vendor=ids))

                data = {
                    'name':name,
                    'products':products
                }
                
            return render(request, 'showpro.html', data)
        
        except:
            return redirect('vlogin')

    def post(self, request):
        message = None
        rmprod = request.POST.get('rmprod')
        prodid = request.POST.get('prodid')
        prodid2 = request.POST.get('prodid2')
        upstock = request.POST.get('upstock')
        upprice = request.POST.get('upprice')

        try:
            if prodid:
                a = Product.objects.get(id=prodid)
                if upprice:
                    new_price = int(upprice)
                    if new_price<0:
                        message = "Invalid Price"
                    else:
                        a.price = new_price
                        # print(new_price)
                        a.save()
                
            if prodid2:
                a = Product.objects.get(id=prodid2)
                if upstock:
                    st = a.stock
                    new_stock = int(st) + int(upstock)
                    if new_stock<=0:
                        p = Product.objects.get(id=prodid)
                        p.delete()
                    else:
                        a.stock = new_stock
                        # print(new_stock)
                        a.save()
                
            if rmprod:
                rmprod = int(rmprod)
                p = Product.objects.get(id=rmprod)
                print("poop:       ", p)
                p.delete()

        except:
            return redirect('showpro')

        ids = int(request.session['vendor'])
        name = Vendor.objects.get(id=ids).name
        print("HOHO:     ",name)
        products = list(Product.objects.filter(vendor=ids))
        data = {
            'naam': name,
            'products': products,
            'error': message
            }
        
        return render(request, 'showpro.html', data)