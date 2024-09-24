from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm  # Importez le formulaire que vous avez créé
from .models import Product  # Assure-toi d'importer le modèle Product
from .forms import ProductForm
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
def BASE(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def afficher_categories(request):
    print("Affichage des catégories")  # Ajoute cette ligne
    categories = Category.objects.all()
    return render(request, 'affichecatg.html', {'categories': categories})



def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('afficher_categories')  # Redirige après ajout de la catégorie
    else:
        form = CategoryForm()  # Formulaire vide pour l'ajout d'une nouvelle catégorie
    
    return render(request, 'ajouter_categorie.html', {'form': form})
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('afficher_categories')  # Remplace par le nom de ta vue pour la liste des catégories
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('afficher_categories')  # Redirige vers la liste des catégories
    else:
        form = CategoryForm(instance=category)  # Pré-remplir le formulaire avec les données de la catégorie
    
    return render(request, 'modifiercategorie.html', {'form': form})
#produit
def afficher_produits(request):
    print("Affichage des produits")  # Ajoute cette ligne pour le débogage
    produits = Product.objects.all()  # Récupère tous les produits
    return render(request, 'afficheprod.html', {'produits': produits})
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Sauvegarde le produit
            return redirect('afficher_produits')  # Redirige vers la liste des produits
    else:
        form = ProductForm()  # Formulaire vide pour l'ajout d'un nouveau produit

    return render(request, 'ajouter_produit.html', {'form': form})  # Render le template
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('afficher_produits')  # Redirige vers la liste des produits
    else:
        form = ProductForm(instance=product)  # Pré-remplir le formulaire avec les données du produit

    return render(request, 'modifierproduit.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Récupère le produit ou retourne 404 s'il n'existe pas
    product.delete()  # Supprime le produit
    return redirect('afficher_produits')  # Redirige vers la liste des produits

def afficher_produit(request):
    produits = Product.objects.all()  # Récupère tous les produits de la base
    return render(request, 'produit.html', {'produits': produits})

def afficher_categorie(request):
    categories = Category.objects.all()  # Récupère toutes les catégories de la base
    return render(request, 'categories.html', {'categories': categories})
def index(request):
    return render(request, 'index.html')
#################################################################################################################
#post et comment

# Afficher la liste des articles (Posts)
def affiche_posts(request):
    posts = Post.objects.all().order_by('-created_at')  # Trier par date
    return render(request, 'gestionpost/affiche_posts.html', {'posts': posts})
#Afficher la liste des articles (Posts) patrie dashboard
def affiche_postsdash(request):
    posts = Post.objects.all()
    return render(request, 'gestionpost/affiche_postdash.html', {'posts': posts})
# Afficher les détails d'un article (Post) avec ses commentaires (Comments)
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'gestionpost/post_detail.html', {'post': post, 'comments': comments, 'form': form})

# Afficher les détails d'un article (Post) avec ses commentaires (Comments) pour dashboard
def post_detail_dash(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('affiche_posts_dash', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'gestionpost/details_post_dash.html', {'post': post, 'comments': comments, 'form': form})

# Ajouter un nouvel article (Post)
def ajouter_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('affiche_posts')
    else:
        form = PostForm()

    return render(request, 'gestionpost/ajouter_post.html', {'form': form})

# Ajouter un nouvel article (Post) dashboard
def ajouter_post_dash(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('affiche_posts_dash')
    else:
        form = PostForm()

    return render(request, 'gestionpost/ajouter_post_dash.html', {'form': form})


# Modifier un article (Post)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('affiche_posts', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'gestionpost/modifier_post.html', {'form': form})


# Modifier un article (Post) dashboard
def edit_post_dash(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail_dash', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'gestionpost/modifier_post_dash.html', {'form': form})

def delete_postdash(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Récupère le produit ou retourne 404 s'il n'existe pas
    post.delete()  # Supprime le produit
    return redirect('affiche_posts_dash')  # Redirige vers la liste des produits

# Supprimer un article (Post)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('affiche_posts')

# Ajouter un commentaire à un article (Post)
def ajouter_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'gestionpost/ajouter_comment.html', {'form': form, 'post': post})


# Supprimer un commentaire
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', post_id=post_id)
    return render(request, 'gestionpost/supprimer_comment.html', {'comment': comment})