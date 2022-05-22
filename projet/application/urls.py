from django.urls import path
from . import views
from .views import HomeView

app_name = 'application'
urlpatterns = [
    path("index/", views.index, name='index'),
    path('', HomeView.as_view(), name='home'),
    path('ajout/', views.ajout, name='ajout'),
    path("traitement/", views.traitement),
    path("affiche/<int:id>/", views.affiche),
    path("delete/<int:id>", views.delete),
    path("update/<int:id>", views.update),
    path("updatetraitment/<int:id>", views.updatetraitment),
    path("ajoutc/", views.ajoutc, name="ajoutc"),
    path("traitementc/", views.traitementc),
    path("updatec/<int:id>", views.updatec),
    path("traitementupdatec/<int:id>", views.traitementupdatec),
    path("affichec/<int:id>", views.affichec),
    path("deletec/<int:id>", views.deletec),
]