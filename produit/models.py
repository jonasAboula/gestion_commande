from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom=models.CharField(max_length=50, null=True)
    description=models.CharField(max_length=200, null=True, blank=True)
    def __str__(self) -> str:
        return self.nom


class Produit(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    nom=models.CharField(max_length=50, null=True)
    categorie=models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL,)
    prix=models.FloatField(max_length=10, null=True)
    stock = models.PositiveIntegerField(default=0)  # Nouvelle ligne

    def __str__(self) -> str:
        return self.nom
    

