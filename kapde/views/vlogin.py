from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from kapde.models.vendor import Vendor


class Vlogin(View):
    def get(self, request):
        try:
            if request.session['vendor']:
                return redirect('add_product')
        except:
            return render(request, 'vlogin.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            vendor = Vendor.objects.get(email=email)
        except:
            vendor = False

        error_message = None

        if vendor:
            flag = check_password(password, vendor.password)

            if flag:
                request.session['vendor'] = vendor.id
                request.session['name'] = vendor.name


                return redirect('showpro')

            else:
                error_message = "Invalid Credentials"
        else:
            error_message = "Invalid Credentials"

        return render(request, 'vlogin.html', {'error': error_message})



def vlogout(request):
    try:
        del request.session['vendor']
        return redirect('vlogin')
    except:
        return redirect('vlogin')