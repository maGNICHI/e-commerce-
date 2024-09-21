from django.contrib import admin
from .models import Category, Product
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'description','date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'description','image','category', 'date_added')
    search_fields = ('title',) 

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)