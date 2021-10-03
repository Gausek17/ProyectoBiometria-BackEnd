from django.shortcuts import render
from .models import Medicion

def mediciones_list(request):
    mediciones = Medicion.objects.all()
    return render(request, 'blog/mediciones_list.html', {'mediciones': mediciones})
