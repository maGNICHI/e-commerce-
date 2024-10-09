from django import forms
from .models import Category, Product, Reclamation, Response  



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'champ-texte'})
        self.fields['description'].widget.attrs.update({'class': 'champ-texte'})


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


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['sujet', 'description', 'priorite']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 10}),
            'sujet': forms.TextInput(attrs={'placeholder': 'Sujet de la réclamation'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReclamationForm, self).__init__(*args, **kwargs)
        self.fields['sujet'].widget.attrs.update({'class': 'champ-texte'})
        self.fields['description'].widget.attrs.update({'class': 'champ-texte'})
        self.fields['priorite'].widget.attrs.update({'class': 'champ-texte'})


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['message', 'reclamation']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 10}),
            'reclamation': forms.Select(attrs={'class': 'champ-texte'}),
        }

    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class': 'champ-texte'})
        self.fields['reclamation'].widget.attrs.update({'class': 'champ-texte'})
