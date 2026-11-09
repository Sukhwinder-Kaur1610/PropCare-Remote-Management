from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
class MaintenanceRequest(models.Model):
    STATUS = [("pending","Pending Approval"),("approved","Approved"),("assigned","Assigned"),("in_progress","In Progress"),("completed","Completed"),("rejected","Rejected")]
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="pending")
    completion_photo = models.ImageField(upload_to="maintenance/completed/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
