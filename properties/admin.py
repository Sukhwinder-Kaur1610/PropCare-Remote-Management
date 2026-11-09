from django.contrib import admin
from .models import Property
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "property_type", "city", "verification_status")
    list_filter = ("property_type", "verification_status", "state")
    search_fields = ("title", "city", "owner__username")
