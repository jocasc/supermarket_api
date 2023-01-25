from rest_framework import serializers
from mercado.models import Produto, Price, Grupo


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'produto', 'grupo', 'taxa']


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class ProductPriceListSerializer(serializers.ModelSerializer):
    # product_name = serializers.ReadOnlyField(source='produto.produto')
    produto = serializers.SerializerMethodField()

    def get_produto(self, obj):
        return obj.product_name.produto

    class Meta:
        model = Price
        exclude = ('id', 'created', 'link_produto', 'product_name',) #'__all__'


class ProductGroupListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ['produto']

