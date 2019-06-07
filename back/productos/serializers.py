from rest_framework import routers, serializers, viewsets
from productos.models import productos

class productosSerializers(serializers.ModelSerializer):
    class Meta:
        model = productos
        fields = ('__all__')