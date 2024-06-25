from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.hashers import make_password , check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


print(make_password('1234')) #give hashedpassword
print(check_password('1234','pbkdf2_sha.............')) #give true or false according to the hashed password match with input value passed bu user



def index(request):
    # print("request recieved")
    # return HttpResponse('<h1>Index Page</h1>')
    # return render(request,'index.html')
    # prds = Product.get_all_products()
    prds = None
    categories = Category.get_all_categories() 
    print(prds)
    #return render(request, 'index.html',{'products':prds})
    #return render(request,'orders/order.html') #if want to render through the the subfolders of templates folder
    # categoryID = request.GET['category']  #Multival dict key error on doing localhost:8000 so we do below one
    categoryID = request.GET.get('category')

    if categoryID:
        prds = Product.get_all_products_by_categoryid(categoryID)
    else:
        prds = Product.get_all_products()
    
    data = {}
    data['products'] = prds
    data['categories'] = categories

    return render(request, 'index.html', data)


def validateCustomer(customer):
    
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


def registerUser(request):
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
       error_message = validateCustomer(customer)

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


def signup(request):
    if request.method == 'GET':
       return render(request,'signup.html')
    
    else:
       return registerUser(request)
        #    return render(request,'signup.html',{'error':error_message})
        #    return HttpResponse("Signup success")  #this email we are getting from name from index.html <input name="email"> so here name plays vital role instead of id



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
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
    