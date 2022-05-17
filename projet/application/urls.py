from django.urls import path
from . import views
from .views import HomeView

app_name = 'application'
urlpatterns = [
    path("index/", views.index, name='index'),
    path('', HomeView.as_view(), name='home'),
    path('pageupdate/', views.pageupdate, name="pageupdate"),
    path('pageedit/', views.pageedit, name="pageedit"),
    path('pagedelete/', views.pagedelete, name="pagedelete"),
    path('ajout/', views.ajout, name='ajout'),
    path("traitement/", views.traitement),
    path("traitement/affiche", views.affiche),
    path("affiche/<int:id>/", views.affiche),
    path("delete/<int:id>", views.delete),
    path("update/<int:id>", views.update),
    path("traitementupdate/<int:id>", views.traitementupdate),
    path("ajoutc/", views.ajoutc),
    path("traitementc/", views.traitementc),
    path("deletec/<int:id>", views.deletec),
]