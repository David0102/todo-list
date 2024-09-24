from django.db import models

class Usuario(models.Model):
    name = models.CharField('Primeiro nome', max_length=255)
    username = models.CharField('Usuário', max_length=255)
    password = models.CharField('Senha', max_length=255)
    is_authenticated = models.BooleanField('Autenticado', default=False)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username