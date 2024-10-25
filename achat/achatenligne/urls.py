from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.BASE, name="dashboard"), 
    path('', views.home,name="home"),
    path('dashboard/categories/', views.afficher_categories, name='afficher_categories'),
    path('dashboard/categories/add/', views.ajouter_categorie, name='ajouter_categorie'),
    path('dashboard/categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('dashboard/categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('dashboard/produits/', views.afficher_produits, name='afficher_produits'),
    path('dashboard/produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('dashboard/produits/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('dashboard/produits/delete/<int:product_id>/', views.delete_product, name='delete_product'),



    #template
    path('produit/', views.afficher_produit, name='afficher_produit'),
    path('', views.index, name='index'),
    path('categorie/', views.afficher_categorie, name='afficher_categorie'),
    
    # Feedback-related URLs for website feedback
    path('dashboard/website-feedbacks/', views.afficher_website_feedbacks, name='afficher_website_feedbacks'),
    path('website-feedback/', views.afficher_website_feedback, name='afficher_website_feedback'),
    path('feedback/add/website/', views.ajouter_website_feedback, name='ajouter_website_feedback'),
    path('dashboard/feedback/delete/website/<int:feedback_id>/', views.delete_website_feedbacks, name='delete_website_feedbacks'),
    path('feedback/delete/website/<int:feedback_id>/', views.delete_website_feedback, name='delete_website_feedback'),
    path('feedback/edit/website/<int:feedback_id>/', views.edit_website_feedback, name='edit_website_feedback'),

# Event CRUD
    path('dashboard/evenements/', views.afficher_evenements, name='afficher_evenements'),
    path('evenement/', views.afficher_evenement, name='afficher_evenement'),

    path('dashboard/evenements/add/', views.ajouter_evenement, name='ajouter_evenement'),
    path('dashboard/evenements/edit/<int:event_id>/', views.edit_evenement, name='edit_evenement'),
    path('dashboard/evenements/delete/<int:event_id>/', views.delete_evenement, name='delete_evenement'),

    # Sponsor CRUD
    path('dashboard/sponsors/', views.afficher_sponsors, name='afficher_sponsors'),
    path('sponsor/', views.afficher_sponsor, name='afficher_sponsor'),


    path('dashboard/sponsors/add/', views.ajouter_sponsor, name='ajouter_sponsor'),
    path('dashboard/sponsors/edit/<int:sponsor_id>/', views.edit_sponsor, name='edit_sponsor'),
    path('dashboard/sponsors/delete/<int:sponsor_id>/', views.delete_sponsor, name='delete_sponsor'),

]
 