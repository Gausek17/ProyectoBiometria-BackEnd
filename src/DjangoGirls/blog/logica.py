


class MedicionDB():

def getTodasLasMediciones():

    return.Medicion.objects.all()

def getUltimasMediciones(int cantidad):

    return ultimas_mediciones = Medicion.objects.filter().order_by('medicion')[:cantidad]
