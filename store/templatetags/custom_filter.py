from django import template


#this register is a decrator
register = template.Library()


@register.filter(name='currency')  #when we use in template then it is called in the below fucntion according matching name this is is use of decrator
def currency(number):   #cart is the dictionary having key values defiend home.html 
    return "Rs."+str(number) 
