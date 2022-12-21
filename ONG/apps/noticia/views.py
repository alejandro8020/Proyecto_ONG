from django.shortcuts import render
from .models import Noticias, Comentarios
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm
from django.urls import reverse_lazy
# Create your views here.

class NoticiaPageView(ListView):
    paginate_by = 4
    model = Noticias
    context_object_name = 'noticias'

def CategoriasView(request,pk):
    categorias_post = Noticias.objects.filter(categoria=pk)
    return render(request, 'noticia/categorias.html',{'cat': pk, 'categorias_post': categorias_post})

class NoticiaDetailView(DetailView):
    model = Noticias

class ComentarioDetailView(CreateView):
    model = Comentarios
    form_class = CommentForm
    template_name = 'noticia/noticias_coment.html'

    def form_valid(self,form):
        form.instance.noticia_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

    success_url = reverse_lazy('home')

    

    






