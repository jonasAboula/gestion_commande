
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import ajouter_au_panier, vider_panier, voir_panier

# urls.py
from django.urls import path
from .views import login_view, logout_view, home_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('inscription/', views.inscription, name='inscription'),
    path('home/', home_view, name='home'),
    path('', home_view, name='index'),  # Rediriger la page d'accueil vers 'home'
    #path('ajouter-au-panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/', views.voir_panier, name='voir_panier'),
    path('vider_panier/', views.vider_panier, name='vider_panier'),
    path('ajouter_au_panier/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('modifier_quantite_panier/', views.modifier_quantite_panier, name='modifier_quantite_panier'),
    path('supprimer_du_panier/', views.supprimer_du_panier, name='supprimer_du_panier'),
  


]


