from django.urls import path
from . import views
app_name = "properties"
urlpatterns = [
    path("", views.property_list, name="list"),
    path("add/", views.property_create, name="add"),
    path("<int:pk>/edit/", views.property_update, name="edit"),
    path("<int:pk>/delete/", views.property_delete, name="delete"),
]
