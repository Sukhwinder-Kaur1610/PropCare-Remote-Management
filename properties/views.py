from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .forms import PropertyForm

@login_required
def property_list(request):
    items = Property.objects.filter(owner=request.user).order_by("-created_at")
    return render(request, "properties/property_list.html", {"properties": items})

@login_required
def property_create(request):
    form = PropertyForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.owner = request.user
        obj.save()
        return redirect("properties:list")
    return render(request, "properties/property_form.html", {"form": form, "heading": "Add Property"})

@login_required
def property_update(request, pk):
    obj = get_object_or_404(Property, pk=pk, owner=request.user)
    form = PropertyForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("properties:list")
    return render(request, "properties/property_form.html", {"form": form, "heading": "Update Property"})

@login_required
def property_delete(request, pk):
    obj = get_object_or_404(Property, pk=pk, owner=request.user)
    if request.method == "POST":
        obj.delete()
        return redirect("properties:list")
    return render(request, "properties/property_confirm_delete.html", {"property": obj})
