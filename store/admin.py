from django.contrib import admin

from .models.product import Product
from .models.category import Category

#SHowing table view with chngaing category object 1 to something else in admin url
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category'] #whatever defiend in model should be named same here also

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
# Register your models here.
admin.site.register(Product,AdminProduct)  # by adding one more parameter adminProduct we can able to see int able view at admin url
admin.site.register(Category, AdminCategory)
