from django.db import models
from uuid import uuid4

def upload_image_cad(instance, filename):
    return f"{instance.id}-{filename}"

# Create your models here.
class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=60, null=True)
    codigo = models.CharField(max_length=60, null=True)
    descricao = models.CharField(max_length=100, null=True)
    imagem = models.ImageField(upload_to=upload_image_cad, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome