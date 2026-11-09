from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
class VerificationCase(models.Model):
    STATUS = [("submitted","Documents Submitted"),("review","Under Review"),("verified","Verified"),("hold","Verification Hold")]
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="verification_cases")
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    identity_document = models.FileField(upload_to="verification/identity/")
    ownership_document = models.FileField(upload_to="verification/ownership/")
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="submitted")
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Verification: {self.property}"
