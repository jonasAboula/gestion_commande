from django.db import models
from produit.models import Produit


class Client(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    telephone = models.CharField(max_length=13, null=True)
    adresse = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    mdp = models.CharField(max_length=50, null=True)

    def __str__(self):
        nom_complet= self.prenom +' '+ self.nom
        return nom_complet

class Panier(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Panier de {self.client}'
    
class LigneDePanier(models.Model):    
    panier = models.ForeignKey(Panier, related_name='lignes', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    quantite = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.quantite > self.produit.stock:
            raise ValueError("Quantité demandée supérieure au stock disponible")
        super().save(*args, **kwargs)
    