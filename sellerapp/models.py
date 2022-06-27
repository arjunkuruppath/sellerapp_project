from django.db import models

# Create your models here.
class regmodel(models.Model):
    usname=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    pswd=models.CharField(max_length=20)

    active=models.BooleanField(null=True, blank=True)          #link send to mail so check mail active user unique email

    def __str__(self):
        return self.usname         #obj1 , obj2 --username

