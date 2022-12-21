from django.shortcuts import render
from .models import Actividad
from django.views.generic import ListView, DetailView

# Create your views here.

class ActividadPageView(ListView):
    paginate_by = 4
    model = Actividad
    context_object_name = 'actividades'
    queryset = Actividad.objects.order_by('-fecha')


class ActividadDetailView(DetailView):
    model = Actividad