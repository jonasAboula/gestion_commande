from django.db import models
from client.models import Client, Panier
from produit.models import Produit, Categorie


# Create your models here.



class Commande(models.Model):
    client=models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    date_commande=models.DateTimeField(auto_now_add=True)
    cout_commande=models.IntegerField(null=True)


    def cout_commande(self):
        return sum(ligne.produit.prix * ligne.quantite for ligne in self.lignes.all())

    def __str__(self):
        return f'Commande de {self.client} du {self.date_commande}'
    
    @property
    def livraison(self):
        return getattr(self, '_livraison', None)

class LigneDeCommande(models.Model):
    commande = models.ForeignKey(Commande, related_name='lignes', on_delete=models.CASCADE, null=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantite} x {self.produit.nom}'
    
    def save(self, *args, **kwargs):
        self.cout_ligne = self.produit.prix * self.quantite
        super().save(*args, **kwargs)

class Livraison(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE, null=True)

    STATUT_CHOICES = (
        ('Non Livré', 'Non Livré'),
        ('Livré', 'Livré'),
    )
    statut=models.CharField(max_length=13, null=True, choices=STATUT_CHOICES, default='Non Livré')
    adresse=models.CharField(max_length=13, null=True, blank=True)
    date_livraison=models.DateField(null=True, blank=True)
    prix_livraison=models.IntegerField(default=2000)

    def __str__(self):
        return f"Livraison #{self.id} - Commande #{self.commande.id} - {self.statut}"

    @property
    def est_livrer(self):
        return self.statut == 'Livré'

#class LigneCommande(models.Model):
#   produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)  # Ajout de la relation avec Produit
#   commande = models.ForeignKey(Commande, null=True, on_delete=models.SET_NULL)  # Ajout de la relation avec Commande
#   prix=models.FloatField(null=True)
#   quantite = models.IntegerField(null=True)