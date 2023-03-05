from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    short_desc = models.CharField(max_length=100,blank=False,null=False)
    desc = models.TextField(blank=False,null=False)
    storage = models.IntegerField(default=10)

    def __str__(self):
        return self.name
    