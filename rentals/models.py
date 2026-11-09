from django.db import models
from properties.models import Property
class RentalListing(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Rental: {self.property}"
