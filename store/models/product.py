from django.db import models
from .category import Category
#class ka first letter uppercase hota hai 
#need toe xtend this Product class to make it as subclass of Model
class Product(models.Model): #now Product is the subclass of Model \
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)  #kisi bhi product fucntion delete karte ho to saarey delete ho jaenge different different category se wo specific product ondelte= 
                                                                # default you clearly know if go to url/admin product we set the default to 1 so that we should not get select an option on doing makemigrations jo category pehle se add hai unme kya add karna chahenge
    # category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT)
     #category will be new option added in add product
    description = models.CharField(max_length=200,default=' ')
    image=models.ImageField(upload_to='uploads/products/') #where to save image if uploaded