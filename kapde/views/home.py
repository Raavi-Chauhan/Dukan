from django.shortcuts import render, redirect
from kapde.models.product import Product
from kapde.models.customer import Customer
from kapde.models.catagory import Catagory
from django.views import View

# Create your views here.

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # print(request.session.get('cart').keys())
        return redirect('home')

    def get(self, request):
        # request.session.clear()
        request.session['order'] = {}
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        products = None
        search = None
        custo = None
        # request.session.get('cart').clear()
        catagories = Catagory.get_all_catagories()
        catagoryID = request.GET.get('catagory')
        search = request.GET.get('search')

        if catagoryID:
            products = Product.get_all_products_by_catagoryid(catagoryID)
        else:
            products = Product.get_all_products();
        
        if search:
            products = Product.get_product_by_search(search);
            # print("You got: ",Products)

        if request.session.get('customer'):
            idoc = request.session['customer']
            custo = Customer.objects.get(id = idoc).first_name
            print("Name = ",custo)
        
        
        data = {}
        data['products'] = products
        data['catagories'] = catagories
        data['Name'] = custo
        print(request.session.get('email'))
        return render(request, 'index.html', data)