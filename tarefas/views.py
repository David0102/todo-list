from django.shortcuts import render, redirect
from tarefas.models import Tarefa
from user.models import Usuario
from datetime import datetime
from django.db import connection
from django.contrib import messages
from django.http import Http404


def criar_tarefa(request):
   if 'username' in request.session:
      username = request.session['username']

      try:
         user = Usuario.objects.get(username=username)

         if user.is_authenticated:
            if request.method == 'POST':
               titulo = request.POST.get('titulo')
               descricao = request.POST.get('descricao')
               data_atual = datetime.now().date()
               user_id = user.id

               query = f"INSERT INTO tarefas (data_criacao, status, user_id, titulo, descricao) VALUES ('{data_atual}', 'pendente', '{user_id}', '{titulo}', '{descricao}');"
               with connection.cursor() as cursor:
                  cursor.execute(query)
               
               messages.success(request, 'Tarefa criada com sucesso.')
               return redirect('index')
            else:
               return redirect('index')
         else:
            return redirect('login')
      except Usuario.DoesNotExist:
         return redirect('login')

def concluir_tarefa(request, id):
   if 'username' in request.session:
      username = request.session['username']

      try:
         user = Usuario.objects.get(username=username)

         if user.is_authenticated:
            query = f"UPDATE tarefas SET status = 'concluida' WHERE id = '{id}'"

            with connection.cursor() as cursor:
               cursor.execute(query)
               rows_affected = cursor.rowcount

            if rows_affected> 0:
               messages.success(request, 'Tarefa marcada como concluída.')
               return redirect('index')
            else:
               raise Http404('Tarefa não encontrada')
         else:
            return redirect('login')
      except Usuario.DoesNotExist:
         return redirect('login')


def remover_tarefa(request, id):
   if 'username' in request.session:
      username = request.session['username']

      try:
         user = Usuario.objects.get(username=username)

         if user.is_authenticated:
            query = f"DELETE FROM tarefas WHERE id = '{id}'"

            with connection.cursor() as cursor:
               cursor.execute(query)
               rows_affected = cursor.rowcount

            if rows_affected > 0: 
               messages.success(request, 'Tarefa removida com sucesso.')
               return redirect('index')
            else:
               raise Http404('Tarefa não encontrada')
         else:
            return redirect('login')
      except Usuario.DoesNotExist:
         return redirect('login')