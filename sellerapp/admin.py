from django.contrib import admin
from .models import User,Product,BuyProduct,SellerData
# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(SellerData)
admin.site.register(BuyProduct)