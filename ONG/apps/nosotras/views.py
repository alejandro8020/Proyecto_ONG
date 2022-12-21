from django.shortcuts import render
from .models import Nosotras
from django.views.generic import ListView

# Create your views here.

class NosotrasPageView(ListView):
    model = Nosotras
    context_object_name = 'nosotras'
# Create your views here.

