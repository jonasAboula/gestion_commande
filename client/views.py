from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Client, Panier, LigneDePanier
from commande.models import Commande, LigneDeCommande
from produit.models import Produit
from django.contrib.auth.hashers import make_password



def home(request):
    return render(request, 'client/home.html')


def panier_count(request):
    if 'client_id' in request.session:
        client_id = request.session['client_id']
        client = Client.objects.get(id=client_id)
        panier = Panier.objects.get(client=client)
        count = LigneDePanier.objects.filter(panier=panier).count()
    else:
        count = 0
    return {'panier_count': count}


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            client = Client.objects.get(email=email, mdp=password)
            request.session['client_id'] = client.id
            return redirect('home')  # Remplacez 'home' par la vue de redirection après connexion
        except Client.DoesNotExist:
            return render(request, 'client/login.html', {'error': 'Email ou mot de passe incorrect'})
    return render(request, 'client/login.html')

def logout_view(request):
    if 'client_id' in request.session:
        del request.session['client_id']
    return redirect('login')


def home_view(request):
    if 'client_id' not in request.session:
        return redirect('login')

    client = Client.objects.get(id=request.session['client_id'])
    Panier.objects.get_or_create(client=client)
    produits = Produit.objects.all

    context={'client':client, 'produits': produits}
    return render(request, 'client/home.html', context)

def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        mdp = request.POST.get('mdp')
        mdp_conf = request.POST.get('mdp_conf')

        if mdp == mdp_conf:
            #hashed_password = make_password(mdp) #crypter le mot de passe meme pour l'admin
            client = Client(nom=nom, prenom=prenom, telephone=telephone, adresse=adresse, email=email, mdp=mdp)
            client.save()
            return redirect('login')
        else:
            return render(request, 'inscription.html', {'error': "Les mots de passe ne correspondent pas"})

    return render(request, 'client/inscription.html')


@csrf_exempt
def ajouter_au_panier(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit_id')
        quantite = int(request.POST.get('quantite', 1))

        if 'client_id' in request.session:
            client_id = request.session['client_id']
            client = Client.objects.get(id=client_id)
            panier, created = Panier.objects.get_or_create(client=client)
            produit = Produit.objects.get(id=produit_id)


            if produit.stock!=0:
                ligne, created = LigneDePanier.objects.get_or_create(panier=panier, produit=produit)
                ligne.quantite += quantite
                ligne.save()

            lignes = LigneDePanier.objects.filter(panier=panier)
            total_items = sum(ligne.quantite for ligne in lignes)

            return JsonResponse({'total_items': total_items})
        else:
            return JsonResponse({'error': 'Client not found in session'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)



def voir_panier(request):
    if 'client_id' not in request.session:
        return redirect('login')

    client = get_object_or_404(Client, id=request.session['client_id'])
    panier = get_object_or_404(Panier, client=client)
    lignes = LigneDePanier.objects.filter(panier=panier)

    total = 0
    lignes_panier = []
    for ligne in lignes:
        if ligne.produit and ligne.produit.prix is not None:
            ligne_total = ligne.produit.prix * ligne.quantite
            total += ligne_total
            lignes_panier.append({
                'ligne_total': ligne_total
            })

    return render(request, 'client/voir_panier.html', {'client': client, 'lignes': lignes, 'total': total})

    #return render(request, 'client/voir_panier.html', {'lignes': lignes, 'total': total})

def vider_panier(request):
    if 'client_id' not in request.session:
        return redirect('login')

    client = get_object_or_404(Client, id=request.session['client_id'])
    panier = get_object_or_404(Panier, client=client)
    LigneDePanier.objects.filter(panier=panier).delete()

    return redirect('voir_panier')

@csrf_exempt
def modifier_quantite_panier(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit_id')
        nouvelle_quantite = int(request.POST.get('quantite', 1))

        if 'client_id' in request.session:
            client_id = request.session['client_id']
            client = Client.objects.get(id=client_id)
            panier = Panier.objects.get(client=client)
            produit = Produit.objects.get(id=produit_id)

            ligne = LigneDePanier.objects.get(panier=panier, produit=produit)
            ligne.quantite = nouvelle_quantite
            ligne.save()

            total_items = sum(ligne.quantite for ligne in LigneDePanier.objects.filter(panier=panier))
            total_cost = sum(ligne.produit.prix * ligne.quantite for ligne in LigneDePanier.objects.filter(panier=panier))

            return JsonResponse({'total_items': total_items, 'total_cost': total_cost})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def supprimer_du_panier(request):
    if request.method == 'POST':
        produit_id = request.POST.get('produit_id')

        if 'client_id' in request.session:
            client_id = request.session['client_id']
            client = Client.objects.get(id=client_id)
            panier = Panier.objects.get(client=client)
            produit = Produit.objects.get(id=produit_id)

            LigneDePanier.objects.filter(panier=panier, produit=produit).delete()

            total_items = sum(ligne.quantite for ligne in LigneDePanier.objects.filter(panier=panier))
            total_cost = sum(ligne.produit.prix * ligne.quantite for ligne in LigneDePanier.objects.filter(panier=panier))

            return JsonResponse({'total_items': total_items, 'total_cost': total_cost})

    return JsonResponse({'error': 'Invalid request'}, status=400)

