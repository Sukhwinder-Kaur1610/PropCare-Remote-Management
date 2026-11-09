from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from properties.models import Property


# Home Page
def landing(request):
    return render(request, "home.html")


# Dashboard Page
@login_required
def home(request):

    properties = Property.objects.filter(
        owner=request.user
    ).order_by("-created_at")

    context = {
        "properties": properties,
        "property_count": properties.count()
    }

    return render(request, "dashboard/home.html", context)