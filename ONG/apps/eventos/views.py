from django.shortcuts import render
from .models import Eventos
from django.views.generic import ListView, DetailView
# Create your views here.

class EventosPageView(ListView):
    paginate_by = 4
    model = Eventos
    context_object_name = 'eventos'


class EventosDetailView(DetailView):
    model = Eventos
