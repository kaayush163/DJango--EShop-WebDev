from django import template


#this register is a decrator
register = template.Library()


@register.filter(name='is_in_cart')  #when we use in template then it is called in the below fucntion according matching name this is is use of decrator
def is_in_cart(product,cart):   #cart is the dictionary having key values defiend home.html 
    
    keys= cart.keys()

    #now writing logic to see whteher product is available in cart or not

    for id in keys:
        print(id,product.id)
        print(type(id),type(product.id))
        #type(id comes string and type(product.id) is int)
        # so covert id to int by int(id)
        if int(id) == product.id:
            return True  #means product is there in cart so return true
    # print(keys)
    # print(product,cart) #product object will print whatever products are there
    #cart also got printed like this   Product object (18) {'1':1,'3':1,'6':1}
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
        
    return 0