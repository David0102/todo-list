from django.shortcuts import render, redirect, get_object_or_404
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

               query = f"INSERT INTO tarefas (titulo, descricao, data_criacao, status, user_id) VALUES ('{titulo}', '{descricao}', '{data_atual}', 'pendente', '{user_id}');"

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
      
#Simula a função get_object_or_404 do django. Mas nesse caso, foi utilizado consulta sql pura, sem orm.
def obter_tarefa_ou_404(tarefa_id, user_id):
    query = "SELECT * FROM tarefas WHERE id = %s AND user_id = %s"
    
    with connection.cursor() as cursor:
        cursor.execute(query, [tarefa_id, user_id])
        tarefa = cursor.fetchone()

    if not tarefa:
        raise Http404("Tarefa não encontrada")
    
    return tarefa

def concluir_tarefa(request, id):
   if 'username' in request.session:
      username = request.session['username']

      try:
         user = Usuario.objects.get(username=username)

         if user.is_authenticated:
            tarefa = obter_tarefa_ou_404(id, user.id)

            query = f"UPDATE tarefas SET status = 'concluida' WHERE id = '{id}'"

            with connection.cursor() as cursor:
               cursor.execute(query)
            
            messages.success(request, 'Tarefa marca como concluída.')
            return redirect('index')
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
            tarefa = obter_tarefa_ou_404(id, user.id)

            query = f"DELETE FROM tarefas WHERE id = '{id}'"

            with connection.cursor() as cursor:
               cursor.execute(query)
            
            messages.success(request, 'Tarefa removida com sucesso.')
            return redirect('index')
         else:
            return redirect('login')
      except Usuario.DoesNotExist:
         return redirect('login')