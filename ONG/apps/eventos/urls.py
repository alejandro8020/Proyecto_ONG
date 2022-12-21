from django.urls import path
from .views import *

urlpatterns = [
    path('', EventosPageView.as_view(), name='eventos'),
    path('<int:pk>/<slug:slug>/', EventosDetailView.as_view(), name='evento'),
    
]