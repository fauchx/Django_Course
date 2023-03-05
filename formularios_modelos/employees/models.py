from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30,blank=False,null=False)
    last_name = models.CharField(max_length=30,blank=False,null=False)
    email = models.EmailField(max_length=70, blank=False,null=False)

    def __str__(self):
        return self.email
    