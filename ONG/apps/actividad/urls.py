from django.urls import path
from .views import *

urlpatterns = [
    path('', ActividadPageView.as_view(), name='actividades'),    
    path('<int:pk>/<slug:slug>/', ActividadDetailView.as_view(), name='actividad'),
]