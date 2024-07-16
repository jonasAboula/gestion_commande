# Generated by Django 5.0.4 on 2024-06-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_remove_client_date_creation_client_adresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='mdp',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='prenom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.CharField(max_length=13, null=True),
        ),
    ]