from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventories.views import  health_check, WarehouseCreationViewSet


router = DefaultRouter()
router.register(r"warehouse-creations", WarehouseCreationViewSet, basename="warehousecreation")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # /api/products/ endpoints
    path("health-check/", health_check),  # /health-check/ endpoints
]
