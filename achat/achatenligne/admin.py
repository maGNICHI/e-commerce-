from django.contrib import admin
from .models import Category, Product,Post,Comment
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'description','date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'description','image','category', 'date_added')
    search_fields = ('title',) 
class AdminComment(admin.ModelAdmin):
    list_display = ('post', 'content','created_at')

class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'content','image', 'created_at')
    search_fields = ('title',) 

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)