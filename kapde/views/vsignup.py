from django.shortcuts import render, redirect
from django.views import View
from kapde.models.vendor import Vendor
from kapde.models.company import Company
from django.contrib.auth.hashers import make_password



class Vsignup(View):
    def get(self, request):

        try:
            if request.session['vendor']:
                return redirect('showpro')

        except:
            companies = Company.objects.all();

            info = {
            'companies' : companies
            }
                
            return render(request,'vsignup.html', info)
    
    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        company = int(request.POST.get('company'))
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        value = {
            'name': name,
            'phone': phone,
            'email': email
        }
        
        try:
            comp = Company.objects.get(id=company)
        except:
            pass

        vendor = Vendor(name=name, phone=phone, email=email, company=comp, password=password)
        error_message = None

        if (len(name)<3):
            error_message = "Enter a valid name!"

        if (len(phone)>12 or len(phone)<7 or int(phone)<0):
            error_message = "Enter valid phone number!"
        
        isExist = Vendor.objects.filter(phone=phone)
        if isExist:
            error_message = "Phone number already exists!"

        if (len(email)<12):
            error_message = "Invalid Email!"

        if (len(password)<8):
            error_message = "Password must be of 8 char!"

        if (password != confirm_password):
            error_message = "Password mismatch"

        isExist = Vendor.objects.filter(email=email)
        if isExist:
            error_message = "Email already exists!"

        if not error_message:
            vendor.password = make_password(vendor.password)
            vendor.save()
            return redirect('add_product')

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'vsignup.html', data)