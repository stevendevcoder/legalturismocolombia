from api.models.interaccion import Interaccion

def verificar_interaccion_real(usuario, prestador):
    """
    Verifica si existe un registro previo de interacción entre el usuario y el prestador
    antes de permitir comentar o calificar.
    """
    return Interaccion.objects.filter(usuario=usuario, prestador=prestador).exists()
