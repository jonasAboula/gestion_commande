from django.forms import ModelForm
from .models import Commande
from django import forms
from .models import LigneDeCommande

class LigneDeCommandeForm(forms.ModelForm):
    class Meta:
        model = LigneDeCommande
        fields = ['produit', 'quantite']

LigneDeCommandeFormSet = forms.inlineformset_factory(
    Commande, LigneDeCommande, form=LigneDeCommandeForm, extra=1, can_delete=True
)
