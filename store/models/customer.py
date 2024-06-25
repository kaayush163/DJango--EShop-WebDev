from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)


    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(self):
        # return Customer.objects.filter(email = self.email)
        try:
            return Customer.objects.get(email=self.email)
        except:
            return False
        # return Customer.objects.get(email = self.email)  # by filter we get list of objects but we want only one object so we use get

    
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False