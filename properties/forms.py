from django import forms
from .models import Property
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ("owner", "verification_status", "created_at")
        widgets = {"address": forms.Textarea(attrs={"rows": 3}), "description": forms.Textarea(attrs={"rows": 3})}
