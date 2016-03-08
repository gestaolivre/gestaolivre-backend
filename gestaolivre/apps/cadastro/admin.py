# -*- coding: utf-8 -*-
u"""Admin do aplicativo de Cadastro."""

from django.contrib import admin

from .forms import EmpresaForm

from .models import Empresa


class EmpresaAdmin(admin.ModelAdmin):
    u"""Admin para Empresa."""

    exclude = ('data',)
    form = EmpresaForm
    list_display = ('nome_fantasia', 'razao_social', 'cnpj')


admin.site.register(Empresa, EmpresaAdmin)
