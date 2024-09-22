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
from django.shortcuts import get_object_or_404, redirect

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
#post et comment


# 1. Lister les articles (Read - Post)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# 2. Afficher les détails d'un article (Read - Post + Comment)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

# 3. Créer un nouvel article (Create - Post)
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

# 4. Mettre à jour un article (Update - Post)
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})

# 5. Supprimer un article (Delete - Post)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

# 6. Mettre à jour un commentaire (Update - Comment)
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form})

# 7. Supprimer un commentaire (Delete - Comment)
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=comment.post.pk)
    return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})
