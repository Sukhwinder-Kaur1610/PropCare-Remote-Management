from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
class Message(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_propcare_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_propcare_messages")
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.sender} → {self.recipient}"
