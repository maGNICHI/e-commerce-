from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm  # Importez le formulaire que vous avez créé
from .models import Product  # Assure-toi d'importer le modèle Product
from .forms import ProductForm
from .models import Reclamation, Response
from .forms import ReclamationForm, ResponseForm

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


# View for front-end
def reclamation_list(request):
    reclamations = Reclamation.objects.all()
    return render(request, 'reclamation/reclamation_list.html', {'reclamations': reclamations})





# Edit a Reclamation
def reclamation_edit(request, pk):
    reclamation = get_object_or_404(Reclamation, pk=pk)
    if request.method == "POST":
        form = ReclamationForm(request.POST, instance=reclamation)
        if form.is_valid():
            form.save()
            return redirect('reclamation_list')
    else:
        form = ReclamationForm(instance=reclamation)
    return render(request, 'reclamation/edit.html', {'form': form})

# Delete a Reclamation
def reclamation_delete(request, pk):
    reclamation = get_object_or_404(Reclamation, pk=pk)
    if request.method == "POST":
        reclamation.delete()
        return redirect('reclamation_list')
    return render(request, 'reclamation/delete.html', {'reclamation': reclamation})

# List responses for a specific Reclamation
def response_list(request, reclamation_id):
    reclamation = get_object_or_404(Reclamation, id=reclamation_id)
    responses = reclamation.responses.all()
    return render(request, 'response_list.html', {'reclamation': reclamation, 'responses': responses})

# Add a new Response
def response_create(request, reclamation_id):
    reclamation = get_object_or_404(Reclamation, id=reclamation_id)
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.reclamation = reclamation
            response.save()
            return redirect('response_list', reclamation_id=reclamation.id)
    else:
        form = ResponseForm()
    return render(request, 'reclamation/response_create.html', {'form': form, 'reclamation': reclamation})

# Edit a Response (optional)
def response_edit(request, reclamation_id, response_id):
    reclamation = get_object_or_404(Reclamation, id=reclamation_id)
    response = get_object_or_404(Response, id=response_id)
    if request.method == "POST":
        form = ResponseForm(request.POST, instance=response)
        if form.is_valid():
            form.save()
            return redirect('response_list', reclamation_id=reclamation.id)
    else:
        form = ResponseForm(instance=response)
    return render(request, 'response_form.html', {'form': form, 'reclamation': reclamation})

# Delete a Response (optional)
def response_delete(request, reclamation_id, response_id):
    response = get_object_or_404(Response, id=response_id)
    if request.method == "POST":
        response.delete()
        return redirect('response_list', reclamation_id=reclamation_id)
    return render(request, 'response_confirm_delete.html', {'response': response})


#daaaachboard

def reclamation_lists(request):
    reclamations = Reclamation.objects.all()
    return render(request, 'reclamation/listreclamation.html', {'reclamations': reclamations})

def edit_reclamation(request, reclamation_id):
    reclamation = get_object_or_404(Reclamation, id=reclamation_id)
    
    if request.method == 'POST':
        form = ReclamationForm(request.POST, instance=reclamation)
        if form.is_valid():
            form.save()
            return redirect('reclamation_lists')  # Redirect to the list view after saving
    else:
        form = ReclamationForm(instance=reclamation)

    return render(request, 'reclamation/editReclamation.html', {'form': form, 'reclamation': reclamation})

# View for deleting a reclamation
def delete_reclamation(request, reclamation_id):
    reclamation = get_object_or_404(Reclamation, id=reclamation_id)
    
    if request.method == 'POST':
        reclamation.delete()
        return redirect('reclamation_lists')  # Redirect to the list view after deletion

    return render(request, 'reclamation/confirm_delete.html', {'reclamation': reclamation})