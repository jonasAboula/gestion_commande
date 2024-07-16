from django.contrib import admin
from .models import Commande, LigneDeCommande, Livraison
from produit.models import Produit

# Register your models here.
#admin.site.register(Commande)
admin.site.register(LigneDeCommande)
#admin.site.register(Livraison)

class LivraisonInline(admin.StackedInline):
    model = Livraison
    can_delete = False
    verbose_name_plural = 'Livraison'

#class ProduitInline(admin.StackedInline):
#    model = Produit
#    can_delete = False
#    verbose_name_plural = 'Produi'

class LigneDeCommandeInline(admin.TabularInline):
    model = LigneDeCommande
    extra = 0  # Pour ne pas ajouter de lignes vides par défaut


class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_commande', 'cout_commande', 'statut_livraison')
    inlines = [LivraisonInline, LigneDeCommandeInline]

    def statut_livraison(self, obj):
            return obj.livraison.statut if obj.livraison else '-'  # Afficher le statut ou '-' si pas de livraison associée

    statut_livraison.short_description = 'Statut de Livraison'  # Libellé de l'en-tête de colonne

admin.site.register(Commande, CommandeAdmin)
admin.site.register(Livraison)