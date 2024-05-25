from django.db import models

#class ka first letter uppercase hota hai 
#need toe xtend this Product class to make it as subclass of Model
class Product(models.Model): #now Product is the subclass of Model \
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200,default=' ')
    image=models.ImageField(upload_to='uploads/products/') #where to save image if uploaded