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
    path('dashboard/post/', views.affiche_posts, name='affiche_posts'),
    path('dashboard/post/ajouter/', views.ajouter_post, name='ajouter_post'),
    path('dashboard/post/edit/<int:id>/', views.edit_post, name='edit_post'),
    path('dashboard/post/delete/<int:id>/', views.delete_post, name='delete_post'),
    #template
    path('produit/', views.afficher_produit, name='afficher_produit'),
    path('', views.index, name='index'),
    path('categorie/', views.afficher_categorie, name='afficher_categorie'),
   
    path('post/', views.affiche_posts, name='affiche_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/ajouter/', views.ajouter_post, name='ajouter_post'),
    path('post/<int:post_id>/modifier/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/supprimer/', views.delete_post, name='delete_post')
]
 