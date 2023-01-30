from rest_framework import serializers
from mercado.models import Produto, Price, Grupo, ListaDeCompras


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaDeCompras
        fields = '__all__'


class ProductPriceListSerializer(serializers.ModelSerializer):
    # product_name = serializers.ReadOnlyField(source='produto.produto')
    produto = serializers.SerializerMethodField()

    def get_produto(self, obj):
        return obj.product_name.produto

    class Meta:
        model = Price
        exclude = ('id', 'created', 'link_produto', 'product_name',)


class ProductGroupListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ['produto']


class ShoppingListSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='produto.produto')
    link_produto = serializers.SerializerMethodField()
    link_imagem = serializers.SerializerMethodField()

    def get_link_produto(self, obj):
        return obj.produto.link_produto

    def get_link_imagem(self, obj):
        return obj.produto.link_imagem

    class Meta:
        model = ListaDeCompras
        fields = ['produto', 'preco', 'product_name', 'link_produto', 'link_imagem']#'__all__'

