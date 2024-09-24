from django import forms
from .models import Category
from .models import Product
from .models import Post, Comment
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




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre du post', 'class': 'champ-texte'}),
            'content': forms.Textarea(attrs={'placeholder': 'Contenu du post', 'rows': 4, 'cols': 10, 'class': 'champ-texte'}),
            'image': forms.ClearableFileInput(attrs={'class': 'champ-texte'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError("Le titre ne peut pas être vide.")
        if len(title) < 5:
            raise ValidationError("Le titre doit contenir au moins 5 caractères.")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError("Le contenu ne peut pas être vide.")
        return content


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Écrivez votre commentaire ici', 'class': 'champ-texte', 'rows': 3, 'cols': 10}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise ValidationError("Le contenu du commentaire ne peut pas être vide.")
        if len(content) < 2:
            raise ValidationError("Le commentaire doit contenir au moins 2 caractères.")
        return content