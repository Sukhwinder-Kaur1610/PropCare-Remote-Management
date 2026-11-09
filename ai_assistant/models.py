from django.db import models
class AssistantLog(models.Model):
    # Placeholder for future AI assistant prompts and responses.
    question = models.TextField()
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"AI request #{self.pk}"
