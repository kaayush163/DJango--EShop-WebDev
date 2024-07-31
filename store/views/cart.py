from django.shortcuts import render , redirect
# Create your views here.

from django.contrib.auth.hashers import check_password
from store .models.customer import Customer
from django.views import View  #importing class

from store.models.product import Product

class Cart(View): #subclass of login is view class
    def get(self,request):
        # pass

        #print(request.session.cart) - this is wrong
        print(request.session.get('cart')) #this is correct
                                           #{'1':1, '2':1 } '1' is product id is showing we need that so 

        print(request.session.get('cart').keys()) #so we get product id in dictionary list
        
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html',{'products':products})
    