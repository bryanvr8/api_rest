from rest_framework import serializers
from meuapp01 import models

class ProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Produto
        fields = '__all__'