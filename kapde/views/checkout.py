from django.shortcuts import redirect
from kapde.models.customer import Customer
from kapde.models.orders import Order
from kapde.models.product import Product
from django.views import View


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        city = request.POST.get('city')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(customer, address, cart, products)


        for product in products:
            a = Product.objects.get(id=product.id)
            st = int(a.stock)
            s = int(a.sale)
            a.stock = st - int(cart.get(str(product.id)))
            a.sale = s + int(cart.get(str(product.id)))
            a.save()
            sa = a.sale
            print("sale bro",sa)

            order = Order(customer=Customer(id = customer), 
                          product = product, 
                          price = product.price,
                          address = address,
                          city = city,
                          quantity = cart.get(str(product.id)))

            order.placeOrder();

        request.session['cart'] = {}

        return redirect('orders')