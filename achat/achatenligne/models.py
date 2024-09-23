from django.db import models
from django.db.models.fields.related import ForeignKey

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
    category = ForeignKey(Category, related_name='produits', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']  

    def __str__(self):
        return self.title 

class WebsiteFeedback(models.Model):
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=1)  # Rating from 1 to 5
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)  # Optional image field


    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"Website Feedback: {self.comment[:20]}..."  # Show first 20 chars

class ProductFeedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Reference to Product
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=1)  # Rating from 1 to 5
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"Feedback for {self.product.title}: {self.comment[:20]}..."  # Show first 20 chars
