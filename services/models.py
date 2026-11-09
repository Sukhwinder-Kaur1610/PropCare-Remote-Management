from django.db import models
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    def __str__(self): return self.name
class ServiceRequest(models.Model):
    STATUS = [("requested","Requested"),("assigned","Assigned"),("completed","Completed")]
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    requested_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE)
    preferred_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="requested")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.service} – {self.property}"
