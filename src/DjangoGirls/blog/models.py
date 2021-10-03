from django.db import models
from django.utils import timezone


class Medicion(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_sensor= models.TextField(default="sensor CO2")
    medicion =models.FloatField()
    fecha = models.DateTimeField(default=timezone.now)
    x = models.FloatField()
    y = models.FloatField()

    def devolverMedicion(self):
        return self.medicion

    def __str__(self):
        return "Medición "+str(self.id) + " - " + str(self.id_sensor)
