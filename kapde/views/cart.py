from django.shortcuts import render, redirect
from kapde.models.product import Product
from django.views import View


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)

        return render(request, 'cart.html', {'products':products})

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        prodrmv = request.POST.get('prodrmv')
        print("Hello ji:",prodrmv)

        if prodrmv:
            cart.pop(prodrmv)

        else:
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


        # ITR = remove_product_by_id(prodlt)

        # if prodlt:
        #     cart.pop(ITR)

        request.session['cart'] = cart
        # print(request.session.get('cart').keys())
        return redirect('cart')