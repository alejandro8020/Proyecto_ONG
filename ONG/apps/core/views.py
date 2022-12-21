from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Testimonios

class TestimonioPageView(ListView):
    model = Testimonios
    context_object_name = 'testimonios'
# Create your views here.