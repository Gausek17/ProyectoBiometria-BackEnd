from django.shortcuts import render
from .models import Medicion
from .logicaNegocio import LogicaNegocio
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def mediciones_list(request):
    mediciones = Medicion.objects.all()
    return render(request, 'blog/mediciones_list.html', {'mediciones': mediciones})

@csrf_exempt
def anyadirMedicion(request):
    if request.method=="POST":

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        medicion = body[0]['medicion']
        longitud = body[0]['longitud']
        latitud = body[0]['latitud']

        LogicaNegocio.guardarMedicion(medicion, longitud, latitud)
    return HttpResponse(status=200)
