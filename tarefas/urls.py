from django.urls import path
from tarefas import views

urlpatterns = [
    path('tarefas/create/', views.criar_tarefa, name='tarefas_create'),
    path('tarefas/update_status/<int:id>', views.concluir_tarefa, name='tarefas_update_status'),
    path('tarefas/delete/<int:id>', views.remover_tarefa, name='tarefas_delete'),
]