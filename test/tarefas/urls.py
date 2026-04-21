from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.home_tarefas,),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('html/', views.html)
]