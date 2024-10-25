from django.contrib import admin
from .models import Category, Product, Event, Sponsor

class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'image', 'category', 'date_added')
    search_fields = ('title',)

class AdminEvent(admin.ModelAdmin):
    list_display = ('event_name', 'start_date', 'end_date', 'location', 'event_type', 'status', 'max_participants')

class AdminSponsor(admin.ModelAdmin):
    list_display = ('name', 'event', 'sponsorship_type', 'description')

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Event, AdminEvent)
admin.site.register(Sponsor, AdminSponsor)
