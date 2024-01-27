from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from clientes.models import Cliente
from clientes.serializer import ClienteSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    """Lista todos os clientes
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter, ]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf', 'rg']
    filterset_fields = ['ativo']
