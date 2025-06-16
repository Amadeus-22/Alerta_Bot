
from django.contrib import admin
from .models import Temperatura, Alerta, LogAlerta

@admin.register(Temperatura)
class TemperaturaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'data_formatada')  # Mostrar valor e data formatada
    list_filter = ('data',)
    search_fields = ('valor',)
    ordering = ('-data',)  # Mostrar os dados mais recentes primeiro

    def data_formatada(self, obj):
        return obj.data.strftime('%d/%m/%Y %H:%M:%S')
    data_formatada.short_description = 'Data'

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ('temperatura', 'data_formatada', 'mensagem')
    list_filter = ('data',)
    search_fields = ('mensagem',)
    ordering = ('-data',)

    def data_formatada(self, obj):
        return obj.data.strftime('%d/%m/%Y %H:%M:%S')
    data_formatada.short_description = 'Data'

@admin.register(LogAlerta)
class LogAlertaAdmin(admin.ModelAdmin):
    list_display = ('data_formatada', 'tipo', 'temperatura', 'mensagem')
    list_filter = ('tipo', 'data')
    search_fields = ('mensagem',)
    ordering = ('-data',)

    def data_formatada(self, obj):
        return obj.data.strftime('%d/%m/%Y %H:%M:%S')
    data_formatada.short_description = 'Data'
