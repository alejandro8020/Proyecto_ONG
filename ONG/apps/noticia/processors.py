from .models import *

def ctx_category(request):
    ctx_category = {}
    ctx_category['categorias'] = Categoria.objects.all()
    #print (ctx_category)
    return ctx_category

def ctx_comentario(request):
    ctx_comentario = {}
    pk = request.resolver_match.kwargs.get('pk')
    ctx_comentario['comentarios'] = Comentarios.objects.filter(noticia=pk)
    #print (ctx_comentario)
    return ctx_comentario

def ctx_noticias(request):
    ctx_noticias = {}
    ctx_noticias['noti'] = Noticias.objects.order_by('fecha')
    #print (ctx_equipo)
    return ctx_noticias