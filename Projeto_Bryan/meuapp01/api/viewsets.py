from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from meuapp01 import models
from meuapp01.api import serializers

class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProdutoSerializers
    queryset = models.Produto.objects.all()
    # permission_classes = (IsAuthenticated,)