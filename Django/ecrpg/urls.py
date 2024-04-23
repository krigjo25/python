from . import views
from django.urls import path

urlpatterns = [
                path('', views.EcRPGIndex, name = 'ecrpg'),
                path('wiki/', views.WikiIndex, name = 'ecrpgwiki'),
                path('banned/', views.bannedPlayer, name='playerBans'),
                path('wiki/<category>/', views.wikiPost, name = 'wikiPost'),
                path('wiki/<int:pk>/', views.WikiDetails, name = 'WikiDetails'),
                path('management/', views.managementTeam, name = 'managementTeam'),
                path('regulations/', views.CommunityRegulations, name = 'regulations'),

]