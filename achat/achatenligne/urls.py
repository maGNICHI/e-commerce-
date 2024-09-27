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

    path('reclamation/reclamation_list/', views.reclamation_list, name='reclamation_list'),

    path('reclamation/Reclamation_form/', views.reclamation_create, name='reclamation_create'),
   path('reclamation/edit/<int:pk>/', views.reclamation_edit, name='reclamation_edit'),
    path('reclamation/delete/<int:pk>/', views.reclamation_delete, name='reclamation_delete'),
    # Other URL patterns
    path('dashboard/reclamation/listreclamation/', views.reclamation_lists, name='reclamation_lists'),
    path('dashboard/reclamation/editReclamation/<int:reclamation_id>', views.edit_reclamation, name='edit_reclamation'),
    path('dashboard/reclamation/deleteReclamation/<int:reclamation_id>/', views.delete_reclamation, name='delete_reclamation'),

    path('dashboard/reclamations/<int:reclamation_id>/responses/', views.response_list, name='response_list'),
    path('dashboard/reclamations/<int:reclamation_id>/responses/add/', views.response_create, name='response_create'),
    path('dashboard/reclamations/<int:reclamation_id>/responses/edit/<int:response_id>/', views.response_edit, name='response_edit'),
    path('dashboard/reclamations/<int:reclamation_id>/responses/delete/<int:response_id>/', views.response_delete, name='response_delete'),
]
 