from .models import *

def ctx_equipo(request):
    ctx_equipo = {}
    ctx_equipo['equipo'] = Equipo.objects.order_by('nombre')
    #print (ctx_equipo)
    return ctx_equipo

