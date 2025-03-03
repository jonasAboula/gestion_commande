# Generated by Django 5.0.4 on 2024-06-05 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0002_alter_commande_statut'),
        ('produit', '0003_alter_produit_categorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='date_creation',
            new_name='date_commande',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='produit',
        ),
        migrations.AddField(
            model_name='commande',
            name='cout_commande',
            field=models.FloatField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='commande',
            name='date_livraison',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='statut',
            field=models.CharField(choices=[('non livré', 'non livré'), ('livré', 'livré')], max_length=40, null=True),
        ),
        migrations.CreateModel(
            name='Ligne_commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(max_length=5, null=True)),
                ('prix', models.IntegerField(max_length=12, null=True)),
                ('commande', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='commande.commande')),
                ('produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produit.produit')),
            ],
        ),
    ]
