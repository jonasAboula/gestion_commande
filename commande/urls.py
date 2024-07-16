
from django.urls import path
from .views import passer_commande, confirmation_commande

urlpatterns = [
    path('passer_commande/', passer_commande, name='passer_commande'),
    path('confirmation-commande/', confirmation_commande, name='confirmation_commande'),

]
