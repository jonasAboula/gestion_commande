# Generated by Django 5.0.4 on 2024-06-07 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_panier'),
        ('produit', '0005_produit_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='LigneDePanier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lignes', to='client.panier')),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produit.produit')),
            ],
        ),
    ]