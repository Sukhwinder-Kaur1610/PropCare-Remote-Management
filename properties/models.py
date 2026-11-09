from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    TYPE_CHOICES = [
        ("house","House / Villa"), ("apartment","Apartment / Flat"), ("shop","Shop / Office"),
        ("plot","Residential Plot"), ("land","Vacant Land"), ("commercial","Commercial / Industrial"),
        ("farmhouse","Farmhouse"), ("other","Other"),
    ]
    STATUS_CHOICES = [("pending","Pending Verification"),("verified","Verified"),("hold","Verification Hold")]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=150)
    property_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=15, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="properties/", blank=True, null=True)
    verification_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} – {self.city}"
