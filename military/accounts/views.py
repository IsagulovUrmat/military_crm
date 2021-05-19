from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializer import *
from rest_framework import viewsets

class DossierViewSet(viewsets.ModelViewSet):

    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer

    def get_queryset(self):
        if isinstance(self.request.user, User):
            dossier = Dossier.objects.filter(user=self.request.user)
            return dossier


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class AuthView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})

