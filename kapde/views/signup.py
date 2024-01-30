from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from kapde.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        try:
            if request.session['customer']:
                return redirect('home')

            if request.session['vendor']:
                return redirect('add_product')
        except:
            return render(request, 'signup.html')
    
    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        error_message = None

        if (len(first_name)<3):
            error_message = "Enter a valid first name!"
        
        if (len(last_name)<3):
            error_message = "Enter a valid last name!"

        if (len(phone)>12 or len(phone)<7 or int(phone)<0):
            error_message = "Enter valid phone number!"
        
        isExist = Customer.objects.filter(phone=phone)
        if isExist:
            error_message = "Phone number already exists!"

        if (len(email)<12):
            error_message = "Invalid Email!"

        if (len(password)<8):
            error_message = "Password must be of 8 char!"

        if (password != confirm_password):
            error_message = "Password mismatch"

        isExist = Customer.objects.filter(email=email)
        if isExist:
            error_message = "Email already exists!"

        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('home')

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)