from django.urls import path
from .views import *

urlpatterns = [
    path('', CursosPageView.as_view(), name='cursos'),
    path('<int:pk>/<slug:slug>/', CursosDetailView.as_view(), name='curso'),
]