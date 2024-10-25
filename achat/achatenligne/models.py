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
    
class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('promotion', 'Promotion'),
        ('seminar', 'Seminar'),
        ('product_launch', 'Product Launch'),
        # Add more event types if needed
    ]

    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    event_name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    max_participants = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    banner_image = models.ImageField(upload_to='event_banners/', blank=True, null=True)  # Make sure this is correct
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name

class Sponsor(models.Model):
    SPONSORSHIP_TYPE_CHOICES = [
        ('financial', 'Financial'),
        ('product', 'Product'),
        # Add more sponsorship types if needed
    ]

    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sponsorship_type = models.CharField(max_length=50, choices=SPONSORSHIP_TYPE_CHOICES)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

