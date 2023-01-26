from rest_framework import viewsets, generics
from mercado.models import Price, Produto, Grupo, ListaDeCompras
# from serializer import ProdutoSerializer, PriceSerializer
from mercado.serializer import ProdutoSerializer, PriceSerializer, \
    ProductPriceListSerializer, ProductGroupListSerializer, ShoppingListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProdutosViewSet(viewsets.ModelViewSet):
    """ Exibir todos os produtos """""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class PriceViewSet(viewsets.ModelViewSet):
    """ Exibir todos os preços """
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ProductPriceList(generics.ListAPIView):
    """ listando os preços de um específico produto """
    def get_queryset(self):
        queryset = Price.objects.filter(product_name=self.kwargs['pk'])
        return queryset
    serializer_class = ProductPriceListSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ProductGroupList(generics.ListAPIView):
    """ listando todos os produtos """
    def get_queryset(self):
        queryset = Produto.objects.filter(grupo=self.kwargs['pk'])
        return queryset
    serializer_class = ProductGroupListSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class ShoppingList(generics.ListAPIView):
    """ listando todos os melhores precos do dia """
    def get_queryset(self):
        queryset = ListaDeCompras.object.all()
        return queryset
    serializer_class = ShoppingListSerializer

