from django.db import models
from django.contrib.auth.models import User
from properties.models import Property
class PropertyExpense(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    recorded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_date = models.DateField()
    invoice = models.FileField(upload_to="expenses/invoices/", blank=True, null=True)
    notes = models.TextField(blank=True)
    def __str__(self): return f"{self.title} – {self.amount}"
