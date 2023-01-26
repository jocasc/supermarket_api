# Generated by Django 4.1.5 on 2023-01-26 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mercado", "0003_remove_price_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ListaDeCompras",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("preco", models.FloatField(default=0)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mercado.produto",
                    ),
                ),
            ],
        ),
    ]
