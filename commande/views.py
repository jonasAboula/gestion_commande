# views.py
from .models import Commande, Produit, LigneDeCommande, Livraison
from django.shortcuts import render, redirect, get_object_or_404
from client.models import Client, Panier, LigneDePanier
from produit.models import Produit


def passer_commande(request):
    if 'client_id' not in request.session:
        return redirect('login')

    client = get_object_or_404(Client, id=request.session['client_id'])
    panier = get_object_or_404(Panier, client=client)
    lignes_panier = LigneDePanier.objects.filter(panier=panier)

    if not lignes_panier.exists():
        return redirect('voir_panier')

    commande = Commande.objects.create(client=client)
    for ligne_panier in lignes_panier:
        LigneDeCommande.objects.create(
            commande=commande,
            produit=ligne_panier.produit,
            quantite=ligne_panier.quantite,
        )
        # Mise à jour du stock
        produit = ligne_panier.produit
        produit.stock -= ligne_panier.quantite
        produit.save()

    livraison, created = Livraison.objects.get_or_create(commande=commande, adresse=client.adresse)
    lignes_panier.delete()
    return redirect('confirmation_commande')



def confirmation_commande(request):
    client = get_object_or_404(Client, id=request.session['client_id'])
    return render(request, 'commande/confirmation_commande.html', {'client':client})

