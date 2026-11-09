from django.db import models
from properties.models import Property
class SaleListing(models.Model):
    property = models.OneToOneField(Property, on_delete=models.CASCADE)
    asking_price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Sale: {self.property}"
