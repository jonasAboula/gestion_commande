# context_processors.py
from .models import Panier, LigneDePanier, Client

def panier_count(request):
    if 'client_id' in request.session:
        client_id = request.session['client_id']
        client = Client.objects.get(id=client_id)
        panier = Panier.objects.get(client=client)
        lignes = LigneDePanier.objects.filter(panier=panier)
        count = sum(ligne.quantite for ligne in lignes)
    else:
        count = 0
    return {'panier_count': count}
