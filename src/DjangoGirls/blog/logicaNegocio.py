from django.db import models
from .models import Medicion


class LogicaNegocio():

    def guardarMedicion(medicion, longitud, latitud):
         medicion= Medicion.objects.create(medicion = medicion, x=longitud, y=latitud)

    def obtenerTodasLasMediciones():

        return Medicion.objects.all()

    def obtenerUltimasMediciones(cantidad):

        return Medicion.objects.filter().order_by('medicion')[:cantidad]
