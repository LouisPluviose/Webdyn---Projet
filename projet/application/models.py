from django.db import models

# Create your models here.


class Avion(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date_production = models.DateField(blank=True, null=True)
    nombre_appareils = models.IntegerField(blank=False)
    presentation = models.TextField(null=True, blank=True)
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"id : {self.id} | {self.nom} est un {self.type}, créé en {self.date_production} à auteur de {self.nombre_appareils} appareils. \n Présentation : {self.presentation}"
        return chaine

    def dico(self):
        return {"nom" : self.nom, "type" : self.type, "date_production" : self.date_production, "nombre_appareils" : self.nombre_appareils, "presentation" : self.presentation, "categorie" : self.categorie}


class Categorie(models.Model):
    usage = models.CharField(max_length=100)
    nomc = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.nomc} est à usage {self.usage}"
        return chaine

    def dico(self):
        return {"nom" : self.nomc, "usage" : self.usage}