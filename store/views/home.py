from django.shortcuts import render,redirect
# from django.http import HttpResponse
# Create your views here.
from store.models.product import Product
from store.models.category import Category
# from .models.customer import Customer
# from django.views import View  #importing class
from django.views import View
class Index(View):

    def post(self, request):
        product = request.POST.get('product')  # this is when we click on add to card same as pass in the name in index.html <input name='product>
        print(product)
        cart = request.session.get('cart')

        if cart:
            # cart[product] = 1
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart printing',request.session['cart'])
        return redirect('homepage')  #rember instead writing like this redirect("http:localhost:8000") we do by setting name parameter in urls.patterns with the same name as here
        
    def get(self,request):
        prds = None
        # request.session.clear()   #this will clear login of user details session also so we have to only clear cart deatils objects only
        #request.session.get('cart').clear()

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
        
        print('you are:',request.session.get('email'))
        return render(request, 'index.html', data)



# def index(request):
    # print("request recieved")
    # return HttpResponse('<h1>Index Page</h1>')
    # return render(request,'index.html')
    # prds = Product.get_all_products()
    # prds = None
    # categories = Category.get_all_categories() 
    # print(prds)
    # #return render(request, 'index.html',{'products':prds})
    # #return render(request,'orders/order.html') #if want to render through the the subfolders of templates folder
    # # categoryID = request.GET['category']  #Multival dict key error on doing localhost:8000 so we do below one
    # categoryID = request.GET.get('category')

    # if categoryID:
    #     prds = Product.get_all_products_by_categoryid(categoryID)
    # else:
    #     prds = Product.get_all_products()
    
    # data = {}
    # data['products'] = prds
    # data['categories'] = categories
    
    # print('you are:',request.session.get('email'))
    # return render(request, 'index.html', data)
