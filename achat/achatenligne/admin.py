from django.contrib import admin
from .models import Category, Product, Reclamation, Response

# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'image', 'category', 'date_added')
    search_fields = ('title',) 

class AdminReclamation(admin.ModelAdmin):
    list_display = ('sujet', 'description', 'priorite', 'date_added')  # Add any other fields you want to display
    search_fields = ('sujet',)  # Add searchable fields if needed

class AdminResponse(admin.ModelAdmin):
    list_display = ('message', 'reclamation', 'date_added')  # Add any other fields you want to display
    search_fields = ('message',)  # Add searchable fields if needed

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Reclamation, AdminReclamation)
admin.site.register(Response, AdminResponse)
