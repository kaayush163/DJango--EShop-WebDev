from django.contrib import admin
from django.urls import path
from .views import index
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index) #this index will call on view.py side
]