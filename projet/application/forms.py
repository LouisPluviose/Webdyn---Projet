from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class AvionForm(ModelForm):
    class Meta:
        model = models.Avion
        fields = {'nom', 'constructeur', 'date_production', 'nombre_appareils', 'presentation', 'categorie'}
        labels = {
            'nom': _('Nom'),
            'constructeur': _('Constructeur'),
            'date_production': _('Date de production'),
            'nombre_appareils': _('Nombre appareils'),
            'presentation': _('Présentation'),
            'categorie': _('Catégorie'),
        }


class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = {'nomc', 'usage'}
        labels = {
            'nomc': _('Nomc'),
            'usage': _('Usage'),
        }
