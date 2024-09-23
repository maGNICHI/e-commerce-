from django import forms
from .models import Category, Product, WebsiteFeedback, ProductFeedback  

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
            empty_label="Sélectionnez une catégorie"  # Option par défaut
        )

class WebsiteFeedbackForm(forms.ModelForm):
    class Meta:
        model = WebsiteFeedback
        fields = ['comment', 'rating','image']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 15, 'placeholder': 'Your feedback'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'placeholder': 'Rate 1-5'}),
            'image': forms.ClearableFileInput(attrs={'class': 'champ-texte'}),
        }

class ProductFeedbackForm(forms.ModelForm):
    class Meta:
        model = ProductFeedback
        fields = ['product', 'comment', 'rating']
        widgets = {
            'product': forms.Select(attrs={'class': 'champ-texte'}),
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 15, 'placeholder': 'Your feedback'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'placeholder': 'Rate 1-5'}),
        }
