
from django.urls import path
from .views import *

urlpatterns = [
    path('', NoticiaPageView.as_view(), name='noticias'),
    path('<int:pk>/<slug:slug>/', NoticiaDetailView.as_view(), name='noticia'),
    path('noticia/<int:pk>/comentario', ComentarioDetailView.as_view(), name='comentario'),
    path('categoria/<int:pk>/', CategoriasView, name='categorias'),
]
