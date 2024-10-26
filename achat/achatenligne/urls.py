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
     # Routes pour Fournisseur
    path('fournisseurs/', views.afficher_fournisseurs, name='afficher_fournisseurs'),
    path('dashboard/fournisseurs/', views.afficher_fournisseurs, name='afficher_fournisseurs'),
    path('dashboard/fournisseurs/ajouter/', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('dashboard/fournisseurs/edit/<int:fournisseur_id>/', views.edit_fournisseur, name='edit_fournisseur'),
    path('dashboard/fournisseurs/delete/<int:fournisseur_id>/', views.delete_fournisseur, name='delete_fournisseur'),

    # Routes pour Commande
    # path('commandes/', views.afficher_commandes, name='afficher_commandes'),
    path('dashboard/commandes/', views.afficher_commandes, name='afficher_commandes'),
    path('dashboard/commandes/ajouter/', views.ajouter_commande, name='ajouter_commande'),
    path('dashboard/commandes/edit/<int:commande_id>/', views.edit_commande, name='edit_commande'),
    path('dashboard/commandes/delete/<int:commande_id>/', views.delete_commande, name='delete_commande'),
    # URLs pour le front (utilisateur)
    # path('produits/', views.liste_produits, name='liste_produits'),
# urls.py
path('commande/ajouter/<int:produit_id>/', views.ajouter_produit_commande, name='ajouter_produit_commande'),
    path('commande/', views.afficher_commande, name='afficher_commande'),
]
 