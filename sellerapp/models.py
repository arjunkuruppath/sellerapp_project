from django.contrib.auth.models import User, UserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

# class Profile(models.Model):
#     user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
#     name = models.CharField(max_length=100,null=True)
#     username = models.CharField(max_length=100,null=True)
#     phone = models.CharField(max_length=100 ,null=True)
#     email = models.CharField(max_length=100,null=True)
#     profile =models.ImageField(upload_to='media',null=True,blank=True)

class User(AbstractUser):
    object = User()
    phone = models.CharField(max_length=100, null=True)
    profile = models.ImageField(upload_to='media', null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.username


class Product(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=100,null=True)
    product_desc = models.CharField(max_length=1000,null=True)
    category = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)
    product_price = models.FloatField(max_length=100,null=True)
    product_img = models.FileField(upload_to='media',null=True,blank=True)
    time = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.product_name
