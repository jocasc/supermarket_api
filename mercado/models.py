from django.db import models

DIFF_CHOICES = (
    (6, 'C'),
    (13, 'D'),
    (23, 'E'),
)


class Grupo(models.Model):
    grupo = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grupo


class Produto(models.Model):
    produto = models.CharField(max_length=128)
    link_produto = models.CharField(max_length=256, null=True)
    link_imagem = models.CharField(max_length=256, null=True)
    link_suggested = models.CharField(max_length=256, null=True)
    name_suggested = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=32, null=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    taxa = models.IntegerField(choices=DIFF_CHOICES)
    preco = models.FloatField(default=0)
    desconto = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.produto


class Price(models.Model):
    product_name = models.ForeignKey(Produto, on_delete=models.CASCADE)
    price_produto = models.FloatField(default=0)
    link_produto = models.CharField(max_length=256, null=True)
    created = models.DateTimeField()

    def __str__(self):
        return f'{self.product_name}'


class ListaDeCompras(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.produto}"




