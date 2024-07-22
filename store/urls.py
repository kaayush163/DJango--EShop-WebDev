from django.contrib import admin
from django.urls import path
# from .views import index,Signup,Login
# from .views import home ,login,signup

from .views.home import Index #class import
from .views.signup import Signup
from .views.login import Login



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
path('login',Login.as_view(), name='login')
]