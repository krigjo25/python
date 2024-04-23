from . import views
from django.urls import path

urlpatterns = [
                path('', views.WebIndex, name = 'index'),
                path('knownledge/', views.BlogIndex, name = 'blogIndex'),
                path('<int:pk>/', views.ProjectDetail, name = 'ProjectDetail'),
                path('knownledge/<category>/', views.blogPost, name = 'blogPost'),

]