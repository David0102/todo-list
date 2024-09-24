from django.db import models
from user.models import Usuario

class Tarefa(models.Model):
    STATUS_CHOICE = [
        ("pendente", "Pendente"),
        ("concluida", "Concluída")
    ]

    titulo = models.CharField("Título", max_length=255)
    descricao = models.TextField("Descrição")
    data_criacao = models.DateField("Criado em")
    status = models.CharField("Status", max_length=10, choices=STATUS_CHOICE, default="pendente")
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tarefas'
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
    
    def __str__(self):
        return self.titulo