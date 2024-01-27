from rest_framework import serializers

from clientes.models import Cliente
from clientes.validators import celular_valido, cpf_valido, nome_valido, rg_valido


class ClienteSerializer(serializers.ModelSerializer):
    """Exibe todos os clientes registrados"""
    
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        nome_valido(data['nome'])
        cpf_valido(data['cpf'])
        rg_valido(data['rg'])
        celular_valido(data['celular'])

        return data