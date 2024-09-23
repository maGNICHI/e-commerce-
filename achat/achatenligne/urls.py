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

    # Feedback-related URLs for product feedback
    path('dashboard/product-feedback/', views.afficher_product_feedback, name='afficher_product_feedback'),
    path('feedback/add/product/', views.ajouter_product_feedback, name='ajouter_product_feedback'),
    path('feedback/delete/product/<int:feedback_id>/', views.delete_product_feedback, name='delete_product_feedback'),
    path('feedback/edit/product/<int:feedback_id>/', views.edit_product_feedback, name='edit_product_feedback'),

]
 