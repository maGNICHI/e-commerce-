from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm  # Importez le formulaire que vous avez créé
from .models import Product  # Assure-toi d'importer le modèle Product
from .forms import ProductForm
from .models import WebsiteFeedback, ProductFeedback  # Importez les modèles de feedback
from .forms import WebsiteFeedbackForm, ProductFeedbackForm  # Importez les formulaires de feedback

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

#feedback

# Display website feedback list
from django.shortcuts import render
from .models import WebsiteFeedback

def afficher_website_feedbacks(request):
    feedbacks = WebsiteFeedback.objects.all()
    total_feedbacks = feedbacks.count()
    total_rating = sum(feedback.rating for feedback in feedbacks)
    average_rating = total_rating / total_feedbacks if total_feedbacks > 0 else 0

    context = {
        'feedbacks': feedbacks,
        'total_feedbacks': total_feedbacks,
        'average_rating': average_rating,
    }
    return render(request, 'afficher_website_feedback.html', context)


def afficher_website_feedback(request):
    feedbacks = WebsiteFeedback.objects.all()
    return render(request, 'website_feedback.html', {'feedbacks': feedbacks})


# Add new website feedback
def ajouter_website_feedback(request):
    if request.method == 'POST':
        form = WebsiteFeedbackForm(request.POST, request.FILES)  # Include request.FILES to handle image uploads
        if form.is_valid():
            form.save()
            return redirect('afficher_website_feedback')
    else:
        form = WebsiteFeedbackForm()

    return render(request, 'ajouter_website_feedback.html', {'form': form})


# Edit existing website feedback
def edit_website_feedback(request, feedback_id):
    feedback = get_object_or_404(WebsiteFeedback, id=feedback_id)
    if request.method == 'POST':
        form = WebsiteFeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('afficher_website_feedback')
    else:
        form = WebsiteFeedbackForm(instance=feedback)

    return render(request, 'modifier_website_feedback.html', {'form': form})

# Delete website feedback
def delete_website_feedbacks(request, feedback_id):
    feedback = get_object_or_404(WebsiteFeedback, id=feedback_id)
    feedback.delete()
    return redirect('afficher_website_feedbacks')

def delete_website_feedback(request, feedback_id):
    feedback = get_object_or_404(WebsiteFeedback, id=feedback_id)
    feedback.delete()
    return redirect('afficher_website_feedback')


# Display product feedback list
def afficher_product_feedback(request):
    feedbacks = ProductFeedback.objects.all()
    return render(request, 'afficher_product_feedback.html', {'feedbacks': feedbacks})

# Add new product feedback
def ajouter_product_feedback(request):
    if request.method == 'POST':
        form = ProductFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('afficher_product_feedback')
    else:
        form = ProductFeedbackForm()

    return render(request, 'ajouter_product_feedback.html', {'form': form})

# Edit existing product feedback
def edit_product_feedback(request, feedback_id):
    feedback = get_object_or_404(ProductFeedback, id=feedback_id)
    if request.method == 'POST':
        form = ProductFeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('afficher_product_feedback')
    else:
        form = ProductFeedbackForm(instance=feedback)

    return render(request, 'modifier_product_feedback.html', {'form': form})

# Delete product feedback
def delete_product_feedback(request, feedback_id):
    feedback = get_object_or_404(ProductFeedback, id=feedback_id)
    feedback.delete()
    return redirect('afficher_product_feedback')