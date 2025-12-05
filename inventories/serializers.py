from rest_framework import serializers
from . import models


        
class WarehouseCreationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id_warehouse_creation', 'name', 'location', 'creation_date', 'update_date', 'inventories',)
        model = models.WarehouseCreation

