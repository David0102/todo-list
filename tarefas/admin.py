from django.contrib import admin
from tarefas.models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'status')
