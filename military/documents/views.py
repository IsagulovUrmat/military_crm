from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from rest_framework import filters
from rest_framework.filters import SearchFilter
from .permissions import IsSuperUserOrReadOnly, FilterObjPermission


class DocumentModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsSuperUserOrReadOnly, FilterObjPermission]
    serializer_class = DocumentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'status', 'text']

    def get_queryset(self):
        try:
            group = self.request.user.groups.all()[0].name
        except IndexError:
            return Document.objects.filter(document_root='public', status='active')

        if group == 'general':
            docs = Document.objects.filter(document_root__in=['public', 'private', 'secret'], status='active')
            return docs
        if group == 'sergeant':
            docs = Document.objects.filter(document_root__in=['public', 'private'], status='active')
            return docs
        if group == 'user':
            docs = Document.objects.filter(document_root__in=['public'], status='active')
            return docs
        if group == 'president':
            docs = Document.objects.filter(document_root__in=['public', 'private', 'secret', 'top-secret'])
            return docs


        def perform_create(self, serializer):
            serializer.save(user=self.request.user)






