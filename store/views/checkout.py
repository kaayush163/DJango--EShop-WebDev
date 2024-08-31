from django.shortcuts import render , redirect
# Create your views here.

from django.contrib.auth.hashers import check_password
from store .models.customer import Customer
from django.views import View  #importing class

from store.models.product import Product
from store.models.orders import Order

class CheckOut(View): #subclass of login is view class
    def post(self,request):
        # pass
        print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        print(address,phone,customer)
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(cart,products)
        
        for product in products:
            # print(cart.get(product.id)) #this will give None as the procut id is showing in string and its quantity is in integer so first change this to string
            print(cart.get(str(product.id)))
            order = Order(customer = Customer(id=customer),   #this is creating customer object by passing the id
                          product = product,
                          price = product.price,
                          address = address,
                          phone = phone,
                          quantity = cart.get(str(product.id)))  #important conversion of string
            # print(order.placeOrder())
            order.save()
        request.session['cart']={}
        
        return redirect('cart')