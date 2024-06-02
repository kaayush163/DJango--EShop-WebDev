from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=20)

    #this def is used for changing the name of category 1 to the actuall category name on product tab in admin url(You can see on the url/admin -> products now changed to category 1 to shirt black or clothes man/ woman)
    def __str__(self):
        return self.name