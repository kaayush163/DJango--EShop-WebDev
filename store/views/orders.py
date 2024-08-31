from django.shortcuts import render , redirect
# Create your views here.

from django.contrib.auth.hashers import check_password
from store .models.customer import Customer
from django.views import View  #importing class

from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware #we use this when there is funnction meqans outside of class inisde of class it is called method not function so we cant not use it instead we use below one
from django.utils.decorators import method_decorator

class OrderView(View):
    # @auth_middleware
    # @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request,'orders.html',{'orders':orders}) #important to pass this orders object so that can be used in zinga template orders.html