from django.contrib import admin
from .models import Product,Contact,Offer,Fruit,Electronic, Xerox, DryFruit, Vegetable, DailyNeed, Stationary

# Register your models here.
admin.site.register(Contact)
admin.site.register(Offer)

class FruitAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ('name','desc')
admin.site.register(Fruit, FruitAdmin)

class DryFruitAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ('name','desc')
admin.site.register(DryFruit, DryFruitAdmin)

class VegetableAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ('name','desc')
admin.site.register(Vegetable, VegetableAdmin)

class DailyNeedAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ('name','desc')
admin.site.register(DailyNeed, DailyNeedAdmin)

class ElectronicAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ('name','desc')
admin.site.register(Electronic, ElectronicAdmin)

class StationaryAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ('name','desc')
admin.site.register(Stationary, StationaryAdmin)

admin.site.register(Xerox)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    search_fields = ('name','desc')
admin.site.register(Product,ProductAdmin)


