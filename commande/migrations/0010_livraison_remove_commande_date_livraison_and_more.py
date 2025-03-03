# Generated by Django 5.0.4 on 2024-06-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0009_remove_commande_lignes_remove_lignedecommande_panier_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(choices=[('Non Livré', 'Non Livré'), ('Livré', 'Livré')], default='Non Livré', max_length=13, null=True)),
                ('adresse', models.CharField(blank=True, max_length=13, null=True)),
                ('date_livraison', models.DateField(blank=True, null=True)),
                ('prix_livraison', models.IntegerField(default=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='commande',
            name='date_livraison',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='statut',
        ),
    ]
