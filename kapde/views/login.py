from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from kapde.models.customer import Customer
from django.views import View


class Login(View):
    def get(self, request): 

        try:
            if request.session['customer']:
                return redirect('home')
        
        except:
            return render(request, 'login.html')
            
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            customer = Customer.objects.get(email=email)
        except:
            customer = False

        error_message = None

        if customer:
            flag = check_password(password, customer.password)
            
            if flag:
                request.session['customer'] = customer.id
                request.session['name'] = customer.first_name
                # Name = customer.first_name
                # print("Name: ",request.session['customer'])
                return redirect('home')
            else:
                error_message = "Invalid Credentials"
        else:
            error_message = 'Invalid Credentials'


        return render(request, 'login.html', {'error': error_message})


def logout(request):
    try:
        del request.session['customer']
        del request.session['cart']
        return redirect('login')
    except:
        return redirect('login')