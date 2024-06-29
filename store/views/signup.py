from django.shortcuts import render , redirect

from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View  #importing class





class Signup(View):
    def get(self,request):
       return render(request,'signup.html')
    def post(self,request):
       print(request.POST) #its giving key value 
       postData = request.POST

       first_name=postData.get('firstname')
       last_name=postData.get('lastname')
       phone=postData.get('phone')
       email=postData.get('email')
       password=postData.get('password')
       
       #validaton
       value = {
           'first_name' : first_name,
           'last_name' : last_name,
           'phone' :phone,
           'email' : email
       }
       error_message=None

       customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)
       error_message = self.validateCustomer(customer)

       #saving
       if not error_message:    
            #2nd methid to sve the custoemrs on signup insteda of models->customer.py
            
            customer.password = make_password(customer.password)
            
            customer.register()       
            return redirect('homepage')
            # return render(request,'index.html')
            # return redirect('http://localhost:8000') #this is not a good method
            # we have to use name in urls.py index 

       else:
           data = {
               'error': error_message,
               'values': value
           } 
           return render(request,'signup.html',data)
    
    def validateCustomer(self,customer):
        error_message = None
        
        if not customer.first_name:
            error_message = "First Name Required"

        elif len(customer.first_name)<4:
            error_message = "First Name must be 4 char long"
        elif not customer.last_name:
            error_message = 'Last Name required'

        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone number must be 10 char long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'

        elif customer.isExists():
            error_message = 'Email already registered'


        return error_message
