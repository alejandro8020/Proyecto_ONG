from .models import *

def ctx_cursos(request):
    ctx_cursos = {}
    ctx_cursos['filtro'] = Cursos.objects.order_by('fecha')
    #print (ctx_equipo)
    return ctx_cursos

