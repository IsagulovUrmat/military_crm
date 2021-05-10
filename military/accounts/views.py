from django.shortcuts import render
from .serializer import *
from rest_framework import viewsets

class DossierViewSet(viewsets.ModelViewSet):

    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

