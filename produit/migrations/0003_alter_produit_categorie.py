# Generated by Django 5.0.4 on 2024-06-05 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_categorie_alter_produit_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produit.categorie'),
        ),
    ]
