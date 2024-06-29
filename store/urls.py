from django.contrib import admin
from django.urls import path
from .views import index,Signup,Login
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index,name='homepage'), #this index will call on view.py side
    # path('signup',signup),
    path('signup',Signup.as_view()),

    # path('login', login)
    path('login', Login.as_view())  #for calling class in views.py


]