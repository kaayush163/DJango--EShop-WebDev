from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models.product import Product
def index(request):
    # print("request recieved")
    # return HttpResponse('<h1>Index Page</h1>')
    # return render(request,'index.html')
    prds = Product.get_all_products() 
    print(prds)
    return render(request, 'index.html',{'products':prds})
    # return render(request,'orders/order.html') #if want to render through the the subfolders of templates folder

