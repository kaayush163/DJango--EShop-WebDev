from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    # if dont do thsi then in products category forign detail from category tables it will shwo like this category(1) or category(2) so we have to convrt this aas string
    # def __str__(self):
    #     return "hello"
    #this def is used for changing the name of category 1 to the actuall category name on product tab in admin url(You can see on the url/admin -> products now changed to category 1 to shirt black or clothes man/ woman)
    def __str__(self):
        return self.name   #name should be same as category table defined in admnin.py