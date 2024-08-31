from django.contrib import admin
from django.urls import path
# from .views import index,Signup,Login
# from .views import home ,login,signup

from .views.home import Index #class import
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart  #Cart class we want to acess here
from .views.checkout import CheckOut
from .views.orders import OrderView

from .middlewares.auth import auth_middleware

urlpatterns = [
    # path('admin/', admin.site.urls),
    #path('',index,name='homepage'), #this index will call on view.py side
    # path('signup',signup),
    #path('signup',Signup.as_view()),

    # path('login', login)
    #path('login', Login.as_view())  #for calling class in views.py

    # path('',home.index,name='homepage' ),
    # path('signup',signup.Signup.as_view(), name = 'signup' ),
    # path('login',login.Login.as_view(), name='login')

    path('',Index.as_view(),name='homepage' ),
    path('signup',Signup.as_view(), name = 'signup' ),
    path('login',Login.as_view(), name='login'),
    path('logout',logout, name='logout'),
    path('cart',Cart.as_view(), name='cart'),
    path('check-out',CheckOut.as_view(),name='checkout'), #we use as as_view when we defiend as class in views/chekout.py
    # path('orders',OrderView.as_view(),name='orders'), #we use as as_view when we defiend as class in views/chekout.py
    path('orders', auth_middleware(OrderView.as_view()),name='orders'), #we use as as_view when we defiend as class in views/chekout.py

]