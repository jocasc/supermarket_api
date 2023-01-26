from django.contrib import admin
from mercado.models import Produto, Price, Grupo, ListaDeCompras


class Produtos(admin.ModelAdmin):
    list_display = ('id', 'grupo', 'taxa', 'created', 'updated')
    list_display_links = ('id',)
    list_per_page = 20


class Prices(admin.ModelAdmin):
    list_display = ['product_name', 'price_produto', 'link_produto', 'created']


admin.site.register(Produto, Produtos)
admin.site.register(Price, Prices)
admin.site.register(Grupo)
admin.site.register(ListaDeCompras)


