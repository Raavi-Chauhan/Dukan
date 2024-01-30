from kapde.models.customer import Customer
from kapde.models.orders import Order
from django.shortcuts import render
from django.views import View


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        order = Order.get_orders_by_customer(customer)
        
        idoc = request.session['customer']
        naam = Customer.objects.get(id = idoc).first_name
        print("naam",naam)

        return render(request, 'orders.html', {'orders':order} )