from django.utils import timezone
from rest_framework import viewsets
from .models import WarehouseCreation
from .serializers import  WarehouseCreationSerializer
from django.db import transaction
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response



class WarehouseCreationViewSet(viewsets.ModelViewSet):
    queryset = WarehouseCreation.objects.all().order_by('id_warehouse_creation')
    serializer_class = WarehouseCreationSerializer
    
    @transaction.atomic
    def perform_create(self, serializer):
        # Crear una sola bodega
        warehouse = serializer.save()

        # Crear muchas bodegas al mismo tiempo
        warehouses_to_create = []

        for _ in range(100):  # Numero de bodegas para crear
            warehouse_to_create = WarehouseCreation(
                name="Bodega{}".format(_), 
                location="Ubicación{}".format(_),
                creation_date=timezone.now(),
                update_date=timezone.now()
            )
            warehouses_to_create.append(warehouse_to_create)

     
        WarehouseCreation.objects.bulk_create(warehouses_to_create)
        return Response({"detail": "Bodegas creadas correctamente."})
    
    @action(detail=False, methods=['post'])
    def create_multiple(self, request):
        
        data = request.data  # Lista de bodegas 
        
        # Validamos y procesamos en un solo bulk create
        warehouses_to_create = []
        for item in data:
            warehouse_to_create = WarehouseCreation(
                name=item['name'],
                location=item['location'],
                creation_date=timezone.now(),
                update_date=timezone.now()
            )
            warehouses_to_create.append(warehouse_to_create)

        WarehouseCreation.objects.bulk_create(warehouses_to_create)
        return Response({"detail": "Bodegas creadas correctamente."})  
        



    
@require_http_methods(["GET", "HEAD"])
def health_check(request):

    res = JsonResponse({"status": "ok"})
    return _no_store(res)
