from django.core.management.base import BaseCommand
from client.models import Client
from commande.models import Commande
from produit.models import Produit

# my_custom_script.py
from faker import Faker
import random
from datetime import timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Génère des données aléatoires et les insère dans la base de données'

    def handle(self, *args, **kwargs):
        # Générer des commandes aléatoires
        for _ in range(30):
            client = random.choice(Client.objects.all())
            produit = random.choice(Produit.objects.all())
            quantite = random.randint(1, 10)
            cout_commande = produit.prix * quantite
            statut = random.choice(["non livré", "livré"])

            # Générer une date de commande aléatoire dans les deux derniers mois
            date_commande = fake.date_time_between(start_date='-2m', end_date='now')

            # Générer une date de livraison si le statut est "livré"
            date_livraison = None
            if statut == "livré":
                # Ajouter un nombre aléatoire de jours à la date de commande pour obtenir la date de livraison
                jours_ajout = random.randint(1, 30)
                date_livraison = date_commande + timedelta(days=jours_ajout)

            Commande.objects.create(
                client=client,
                produit=produit,
                quantite=quantite,
                cout_commande=cout_commande,
                statut=statut,
                date_commande=date_commande,
                date_livraison=date_livraison
            )
