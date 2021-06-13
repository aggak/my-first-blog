from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.detail_article, name='detail_article'),
    path('ecrire_article/', views.ecrire_article, name='ecrire_article'),
    path('modifier_article/<int:pk>/', views.modifier_article, name='modifier_article'),
    path('draft/', views.draft, name='draft'),
    path('publish/<int:pk>/', views.publish, name='publish'),
    path('supprimer/<int:pk>/', views.supprimer_article, name='supprimer_article'),
    path('approuver_commentaire/<int:pk>/', views.approuver_commentaire, name='approuver_commentaire'),
    path('supprimer_commentaire/<int:pk>/', views.supprimer_commentaire, name='supprimer_commentaire'),
    

]
