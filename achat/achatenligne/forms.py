from django import forms
from .models import Category, Product, WebsiteFeedback,Event,Sponsor

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

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'description', 'start_date', 'end_date', 'location', 'event_type', 'max_participants', 'status', 'banner_image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 10}),
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['name', 'event', 'sponsorship_type', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 10}),
        }
