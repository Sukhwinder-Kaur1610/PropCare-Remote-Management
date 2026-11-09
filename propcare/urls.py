from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import landing

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing, name="home"),
    path("accounts/", include("accounts.urls")),
    path("properties/", include("properties.urls")),
    path("verification/", include("verification.urls")),
    path("inspections/", include("inspections.urls")),
    path("maintenance/", include("maintenance.urls")),
    path("services/", include("services.urls")),
    path("rentals/", include("rentals.urls")),
    path("sales/", include("sales.urls")),
    path("payments/", include("payments.urls")),
    path("notifications/", include("notifications.urls")),
    path("messages/", include("messaging.urls")),
    path("dashboard/", include("dashboard.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
