from rest_framework.serializers import ModelSerializer

from garagem.models import Acessorio, Categoria, Cor, Marca, Veiculo


class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"


class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1


class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["modelo", "ano", "preco"]
