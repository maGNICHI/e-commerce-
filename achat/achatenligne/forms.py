from django import forms
from .models import Category, Product, Fournisseur, Commande

# Formulaire pour la catégorie
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'champ-texte'})
        self.fields['description'].widget.attrs.update({'class': 'champ-texte'})


# Formulaire pour le produit
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'description', 'category', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 10}),
            'title': forms.TextInput(attrs={'placeholder': 'Nom du produit'}),
            'price': forms.TextInput(attrs={'placeholder': 'Prix'}),
            'image': forms.ClearableFileInput(attrs={'class': 'champ-texte'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'champ-texte'})
        self.fields['price'].widget.attrs.update({'class': 'champ-texte'})
        self.fields['description'].widget.attrs.update({'class': 'champ-texte'})
        self.fields['image'].widget.attrs.update({'class': 'champ-texte'})
        self.fields['category'] = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            widget=forms.Select(attrs={'class': 'champ-texte'}),
            empty_label="Sélectionnez une catégorie" 
        )


# Formulaire pour le fournisseur
class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'email_contact', 'telephone_contact', 'adresse']


# Formulaire pour la commande
class CommandeForm(forms.ModelForm):
    produit = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        label="Produit",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    statut = forms.ChoiceField(
        choices=Commande.STATUT_CHOIX,
        label="Statut",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Commande
        fields = ['utilisateur', 'produit', 'statut', 'prix_total']
