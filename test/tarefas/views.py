from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_tarefas(request):
    context = {
        'nome' : 'Eddie ',
    }
    return render(request, 'tarefas/tarefas.html', context)

def adicionar(request):
    return HttpResponse("<h1>Add new tasks</h1>",)

def html(request):
    return render(request,'tarefas/fodao.html',)