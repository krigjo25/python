from django.urls import path
from hello.views import HelloWorld

urlpatterns = [

    path('', HelloWorld, name='hello'),

]