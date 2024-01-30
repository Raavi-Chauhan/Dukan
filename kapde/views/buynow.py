from django.shortcuts import redirect
from kapde.models.customer import Customer
from kapde.models.orders import Order
from kapde.models.product import Product
from django.views import View


class BuyNow(View):
    def post(self, request):
        address = request.POST.get('address')
        city = request.POST.get('city')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(customer, address, cart, products)

        for product in products:
            order = Order(customer=Customer(id = customer), 
                          product = product, 
                          price = product.price,
                          address = address,
                          city = city,
                          quantity = cart.get(str(product.id)))

            order.placeOrder();

        request.session['cart'] = {}

        return redirect('orders')