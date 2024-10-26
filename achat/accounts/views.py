from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import ClientSignUpForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages  # Import pour ajouter des messages d'erreur

# Vue pour l'inscription d'un client
def register_client(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirige après inscription
    else:
        form = ClientSignUpForm()
    return render(request, 'register.html', {'form': form})  # Utilise le template register.html


# Fonction pour vérifier si l'utilisateur est admin
def admin_required(user):
    return user.is_authenticated and user.is_admin

# Vue pour le tableau de bord admin
@user_passes_test(admin_required)
def dashboard_view(request):
    return render(request, 'admin_dashboard.html')

# Vue pour la connexion


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_admin:
                    return redirect('admin_dashboard')
                elif user.is_client:
                    return redirect('home')
                else:
                    return redirect('home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")  # Ajoute un message d'erreur
        else:
            messages.error(request, "Formulaire invalide. Vérifiez les informations fournies.")

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




