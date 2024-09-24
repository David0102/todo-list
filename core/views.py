from django.shortcuts import render, redirect
from tarefas.models import Tarefa
from user.models import Usuario

def index(request):
    if 'username' in request.session:
        username = request.session['username']
        
        try:
            user = Usuario.objects.get(username=username)
            
            if user.is_authenticated:
                tarefas = Tarefa.objects.filter(user=user)
                context = {
                    'usuario':user,
                    'tarefas':tarefas,
                }
                return render(request, 'index.html', context)
            else:
                return redirect('login')
        except Usuario.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')