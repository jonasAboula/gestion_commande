# my_custom_script.py
from django.core.management.base import BaseCommand
from client.models import Client, Produit
from commande.models import Commande, LigneDeCommande, Livraison
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Génère des données aléatoires et les insère dans la base de données'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Générer des clients
        for _ in range(5):
            client = Client(
                nom=fake.last_name(),
                prenom=fake.first_name(),
                telephone=fake.phone_number(),
                adresse=fake.address(),
                email=fake.email(),
                mdp=fake.password()
            )
            client.save()

        # Générer des produits
       # for _ in range(10):
       #     produit = Produit(
       #         nom=fake.word(),
       #         categorie=fake.word(),
       #         prix=random.uniform(5.0, 100.0),
       #         stock=random.randint(1, 100),
       #         image='path/to/default/image.jpg'
       #     )
       #     produit.save()

        # Générer des commandes et des lignes de commandes et livraisons
        clients = Client.objects.all()
        produits = Produit.objects.all()

        for _ in range(3):
            client = random.choice(clients)
            date_commande = fake.date_time_between(start_date='-2m', end_date='now', tzinfo=timezone.get_current_timezone())
            commande = Commande(
                client=client,
                date_commande=date_commande,
            )
            commande.save()

            num_lignes = random.randint(1, 5)
            total_cout = 0
            for _ in range(num_lignes):
                produit = random.choice(produits)
                quantite = random.randint(1, 10)
                ligne = LigneDeCommande(
                    commande=commande,
                    produit=produit,
                    quantite=quantite,
                )
                ligne.save()
                total_cout += produit.prix * quantite

            commande.total_cout = total_cout

            if random.choice([True, False]):
                date_livraison = date_commande + timedelta(days=random.randint(1, 14))
                livraison = Livraison(
                    commande=commande,
                    adresse=fake.address(),
                    date_livraison=date_livraison,
                )
                livraison.save()

        self.stdout.write(self.style.SUCCESS('Données générées avec succès.'))
