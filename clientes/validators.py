from rest_framework import serializers


def cpf_valido(cpf):
    """Lib validate-docbr para validacao de documento do Brasil"""
    if len(cpf) != 11:
        raise serializers.ValidationError({'cpf':'O cpf não é válido, corrijá e tente novamente'})

def nome_valido(nome: str):
    if nome.split() ==  '' or not nome.isalpha():
        raise serializers.ValidationError({'nome':'Nome inválido, corrijá e tente novamente.'})        

def rg_valido(rg):
    if len(rg) != 9:
        raise serializers.ValidationError({'rg':'O RG de conter exatamente 9 dígitos'})

def celular_valido(celular):
    import re
    
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    
    if not resposta:
        raise serializers.ValidationError({'celular':'O celular não é válido, corrija e tente novamente ex: 11 91234-4321'})
    
