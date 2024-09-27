from django.db import models
from django.db.models.fields.related import ForeignKey

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


class Reclamation(models.Model):
    PRIORITE_CHOICES = [
        (1, 'Faible'),
        (2, 'Moyenne'),
        (3, 'Haute'),
    ]
    
    sujet = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    priorite = models.IntegerField(choices=PRIORITE_CHOICES, default=2)  # Priorité par défaut "Moyenne"

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return f'{self.sujet} - Priorité: {self.get_priorite_display()}' 


class Response(models.Model):
    message = models.TextField()
    date_response = models.DateTimeField(auto_now_add=True)
    reclamation = ForeignKey(Reclamation, related_name='responses', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_response']

    def __str__(self):
        return f'Response to {self.reclamation.sujet} on {self.date_response}'
