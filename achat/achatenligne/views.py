from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm  
from .models import Product  
from .forms import ProductForm
from .models import Fournisseur, Commande, ÉlémentCommande
from .forms import FournisseurForm, CommandeForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal

# Create your views here.
def BASE(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def afficher_categories(request):
    print("Affichage des catégories")  
    categories = Category.objects.all()
    return render(request, 'affichecatg.html', {'categories': categories})
def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('afficher_categories') 
    else:
        form = CategoryForm()  
    
    return render(request, 'ajouter_categorie.html', {'form': form})
 
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('afficher_categories')  
 
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('afficher_categories') 
    else:
        form = CategoryForm(instance=category) 
    
    return render(request, 'modifiercategorie.html', {'form': form})
#produit
def afficher_produits(request):
    print("Affichage des produits")  
    produits = Product.objects.all()  
    return render(request, 'afficheprod.html', {'produits': produits})
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('afficher_produits')  
    else:
        form = ProductForm() 

    return render(request, 'ajouter_produit.html', {'form': form})  
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('afficher_produits')  
    else:
        form = ProductForm(instance=product)  

    return render(request, 'modifierproduit.html', {'form': form})
from django.shortcuts import get_object_or_404, redirect

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  
    product.delete()  
    return redirect('afficher_produits')  

def afficher_produit(request):
    produits = Product.objects.all()  
    return render(request, 'produit.html', {'produits': produits})

def afficher_categorie(request):
    categories = Category.objects.all() 
    return render(request, 'categories.html', {'categories': categories})
def index(request):
    return render(request, 'index.html')
# Vues pour Fournisseur
def afficher_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'afficher_fournisseurs.html', {'fournisseurs': fournisseurs})

def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('afficher_fournisseurs')
    else:
        form = FournisseurForm()
    return render(request, 'ajouter_fournisseur.html', {'form': form})

def edit_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, id=fournisseur_id)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('afficher_fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'modifier_fournisseur.html', {'form': form})

def delete_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, id=fournisseur_id)
    fournisseur.delete()
    return redirect('afficher_fournisseurs')

# Vues pour Commande
def afficher_commandes(request):
    commandes = Commande.objects.all()
    return render(request, 'afficher_commandes.html', {'commandes': commandes})

# def ajouter_commande(request):
#     if request.method == 'POST':
#         form = CommandeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('afficher_commandes')
#     else:
#         form = CommandeForm()
#     return render(request, 'ajouter_commande.html', {'form': form})
@login_required
def ajouter_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save(commit=False)
            commande.utilisateur = request.user  # Associe la commande à l'utilisateur connecté
            commande.save()
            messages.success(request, "Commande ajoutée avec succès !")
            return redirect('afficher_commandes')
    else:
        form = CommandeForm()
    return render(request, 'ajouter_commande.html', {'form': form})

def edit_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('afficher_commandes')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'modifier_commande.html', {'form': form})

def delete_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    commande.delete()
    return redirect('afficher_commandes')
# Vue pour ajouter un produit à la commande de l'utilisateur dans le front-end

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Commande, ÉlémentCommande
from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Commande, ÉlémentCommande
from decimal import Decimal

def ajouter_produit_commande(request, produit_id):
    produit = get_object_or_404(Product, id=produit_id)

    # Créer ou récupérer une commande en cours pour l'utilisateur
    commande, created = Commande.objects.get_or_create(
        utilisateur=request.user,
        statut='EN_COURS',
        defaults={'prix_total': Decimal('0.00')}  # Initialisez prix_total à 0.00 comme Decimal
    )

    # Vérifiez si l'élément de commande existe déjà
    element_commande, created = ÉlémentCommande.objects.get_or_create(
        commande=commande,
        produit=produit,
        defaults={'quantité': 0, 'prix': produit.price}
    )

    # Mise à jour de la quantité et du prix
    element_commande.quantité += 1
    element_commande.prix = produit.price  # Assurez-vous que le prix est le prix actuel du produit
    element_commande.save()

    # Mise à jour du prix total de la commande
    commande.prix_total += Decimal(produit.price)  # Convertir le prix du produit en Decimal
    commande.save()  # Enregistrez la commande avec le prix mis à jour

    # Affichez le message de succès uniquement si c'est un nouvel élément de commande
    if created:
        messages.success(request, f'{produit.title} a été ajouté à votre commande.')
    else:
        messages.info(request, f'La quantité de {produit.title} a été mise à jour dans votre commande.')

    return redirect('afficher_produit')  # Redirige vers l'affichage des produits


# Vue pour afficher la commande (ou panier) de l'utilisateur
def afficher_commande(request):
    commande = Commande.objects.filter(utilisateur=request.user, statut='EN_COURS').first()
    elements_commande = ÉlémentCommande.objects.filter(commande=commande) if commande else None
    return render(request, 'commande.html', {'commande': commande, 'elements_commande': elements_commande})