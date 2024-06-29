from django.shortcuts import render , redirect
# Create your views here.

from django.contrib.auth.hashers import check_password
from store .models.customer import Customer
from django.views import View  #importing class


class Login(View): #subclass of login is view class
    def get(self,request):
        # pass
        return render(request, 'login.html')


    def post(self,request):
        #pass  
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)

            if flag:
                # pass
                return redirect('homepage')
            else:
                error_message = 'Email or Password is invalid'
        else:
            error_message = 'Email or Password is invalid'

        
        print(customer)
        print(email,password)

        return render(request, 'login.html',{'error':error_message}) 
