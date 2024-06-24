from django.contrib import admin

from .models.product import Product
from .models.category import Category
from .models.customer import Customer
#SHowing table view with chngaing category object 1 to something else in admin url
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category'] #whatever defiend in model should be named same here also

#if we dont do thsi category then it will show like this category(1) caetgory(2) not showing the actual category name cloths-men
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# class AdminCustomer(admin.ModelAdmin):
#     list_display = ['first_name','last_name','phone','email','password']
# Register your models here.
admin.site.register(Product,AdminProduct)  # by adding one more parameter adminProduct we can able to see int able view at admin url
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)