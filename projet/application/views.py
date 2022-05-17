from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import AvionForm
from . import models
from django.http import HttpResponseRedirect
from .forms import AvionForm
from .forms import CategorieForm


# Create your views here.


class HomeView(TemplateView):
    template_name = 'main.html'


def ajout(request):
    if request.GET.get("POST"):
        form = AvionForm(request)
        if form.is_valid():
            livre = form.save()
            return HttpResponseRedirect("/application/")
        else:
            return render(request,"application/ajout.html",{"form": form})
    else :
        form = AvionForm()
        return render(request,"application/ajout.html",{"form" : form})


def traitement(request):
    lform = AvionForm(request.POST)
    if lform.is_valid():
        avion = lform.save()
        return HttpResponseRedirect("/application/affiche")
    else:
        return render(request,"application/ajout.html",{"form": lform})


def index(request):
    liste = list(models.Avion.objects.all())
    return render(request, 'application/index.html', {'liste': liste})


def affiche(request, id):
    avion = models.Avion.objects.get(pk=id)
    return render(request,"application/affiche.html",{"avion" : avion})


def pageedit(request):
    return render(request, "application/pageedit.html")


def pagedelete(request):
    return render(request, "application/pagedelete.html")


def pageupdate(request):
    if request.GET.get("POST"):
        form = AvionForm(request)
        if form.is_valid():
            return HttpResponseRedirect("/application/update/", {"id" : id})
        else:
            return render(request, "application/pageupdate.html", {"form": form})
    else:
        form = AvionForm()
        return render(request, "application/pageupdate.html", {"form": form})


def delete(request, id):
    avion = models.Avion.objects.get(pk=id)
    avion.delete()
    return HttpResponseRedirect("/application/")


def update(request, id):
    avion = models.Avion.objects.get(pk=id)
    lform = AvionForm(avion.dico())
    return render(request, "application/update.html", {"form": lform, "id": id})


def traitementupdate(request, id):
    lform = AvionForm(request.POST)
    if lform.is_valid():
        avion = lform.save(commit=False)
        avion.id = id
        avion.save()
        return HttpResponseRedirect("/application/")
    else:
        return render(request, "application/update.html", {"form": lform, "id": id})


################################################################


def ajoutc(request):
    if request.GET.get("POST"):
        form = CategorieForm(request)
        if form.is_valid():
            livre = form.save()
            return HttpResponseRedirect("/application/")
        else:
            return render(request,"application/ajoutc.html",{"form": form})
    else :
        form = CategorieForm()
        return render(request,"application/ajoutc.html",{"form" : form})


def traitementc(request):
    lform = CategorieForm(request.POST)
    if lform.is_valid():
        avion = lform.save()
        return HttpResponseRedirect("/application/index/")
    else:
        return render(request,"application/ajoutc.html",{"form": lform})


def deletec(request, id):
    avion = models.Categorie.objects.get(pk=id)
    avion.delete()
    return HttpResponseRedirect("/application/index/")