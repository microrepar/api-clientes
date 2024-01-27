from django.contrib import admin

from clientes.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'celular', 'ativo')
    list_display_links = ('id', 'nome', 'cpf', 'rg', 'celular')
    search_fields = ('nome', 'cpf', 'rg')
    list_editable = ('ativo',)
    list_per_page = 10
    ordering = ('nome',)

admin.site.register(Cliente, ClienteAdmin)