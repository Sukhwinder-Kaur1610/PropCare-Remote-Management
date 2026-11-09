from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
class Inspection(models.Model):
    STATUS = [("requested","Requested"),("assigned","Assigned"),("completed","Completed"),("cancelled","Cancelled")]
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inspection_requests")
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="managed_inspections")
    scheduled_for = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="requested")
    checklist_notes = models.TextField(blank=True)
    report = models.TextField(blank=True)
    photo = models.ImageField(upload_to="inspections/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Inspection – {self.property}"
