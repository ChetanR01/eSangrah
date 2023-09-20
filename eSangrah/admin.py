from django.contrib import admin
from .models import Product,Contact,Offer,Fruit

# Register your models here.
admin.site.register(Contact)
admin.site.register(Offer)

class FruitAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ('name','desc')
admin.site.register(Fruit, FruitAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ('name','desc')
admin.site.register(Product,ProductAdmin)


