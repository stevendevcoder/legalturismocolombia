from api.models.interaccion import Interaccion

def verificar_interaccion_real(usuario, prestador):

    return Interaccion.objects.filter(usuario=usuario, prestador=prestador).exists()
