from django.db import models
from django.db.models.fields.related import ForeignKey
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name    


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_added']  

    def __str__(self):
        return self.title 

# Entité Fournisseur
class Fournisseur(models.Model):
    nom = models.CharField(max_length=255)
    email_contact = models.EmailField()
    telephone_contact = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.nom


# Entité Commande
class Commande(models.Model):
    STATUT_CHOIX = [
        ('en_attente', 'En attente'),
        ('traitée', 'Traitée'),
        ('expédiée', 'Expédiée'),
        ('livrée', 'Livrée'),
        ('annulée', 'Annulée'),
    ]

    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=STATUT_CHOIX, default='en_attente')
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Valeur par défaut ajoutée

    class Meta:
        ordering = ['-date_commande']

    def __str__(self):
        return f"Commande #{self.id} par {self.utilisateur.username}"

# Entité ÉlémentCommande (Jointure entre Commande et Produit)
class ÉlémentCommande(models.Model):
    commande = models.ForeignKey(Commande, related_name='éléments', on_delete=models.CASCADE)
    produit = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantité = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('commande', 'produit')  # Assure l'unicité d'un produit par commande
        verbose_name = "Élément de Commande"
        verbose_name_plural = "Éléments de Commande"

    def __str__(self):
        return f"{self.quantité} x {self.produit.titre} dans la commande #{self.commande.id}"