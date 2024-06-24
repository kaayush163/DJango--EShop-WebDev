from django.contrib import admin
from django.urls import path
from .views import index,signup
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index), #this index will call on view.py side
    path('signup',signup)
]