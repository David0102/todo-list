from django.urls import path
from tarefas import views

urlpatterns = [
    path('tarefas/create/', views.criar_tarefa, name='tarefas_create'),
    path('tarefas/update_status/<str:id>', views.concluir_tarefa, name='tarefas_update_status'),
    path('tarefas/delete/<str:id>', views.remover_tarefa, name='tarefas_delete'),
]