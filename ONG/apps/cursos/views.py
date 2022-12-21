from django.shortcuts import render
from .models import Cursos
from django.views.generic import ListView, DetailView
# Create your views here.

class CursosPageView(ListView):
    paginate_by = 4
    model = Cursos
    context_object_name = 'cursos'
    queryset = Cursos.objects.order_by('fecha')


class CursosDetailView(DetailView):
    model = Cursos
