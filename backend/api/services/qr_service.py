import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from api.models.prestador import PrestadorServicio


def generar_qr_para_prestador(prestador):
    """
    Genera un código QR para un prestador con su ID
    """
    data = f"PRESTADOR_ID:{prestador.id}"

    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    nombre_archivo = f"qr_prestador_{prestador.id}.png"
    prestador.qr.save(nombre_archivo, ContentFile(buffer.getvalue()), save=True)

    return prestador.qr.url


def obtener_datos_prestador_por_qr(data_qr):
    """
    Extrae el ID del prestador desde el QR y retorna el prestador
    """
    if not data_qr.startswith("PRESTADOR_ID:"):
        return None

    prestador_id = data_qr.replace("PRESTADOR_ID:", "")
    try:
        return PrestadorServicio.objects.get(id=prestador_id)
    except PrestadorServicio.DoesNotExist:
        return None