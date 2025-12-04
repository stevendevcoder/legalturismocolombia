from django.db.models import QuerySet
from django.utils import timezone
from typing import Optional

from legalturismocolombia.backend.api import models

from ..models.calificacion import CalificacionServicioUsuario
from ..models.servicio import CardServicioVenta
from ..models.turista import Turista


class CalificacionRepository:
    """
    Repositorio que encapsula toda la lógica de acceso a datos
    para el modelo CalificacionServicioUsuario.
    """

    # -----------------------------
    # CRUD BÁSICO
    # -----------------------------
    @staticmethod
    def crear_calificacion(
        puntuacion_general: str,
        feedback_empresa: str,
        puntuacion_certificados: str,
        calificacion_puntualidad: str,
        calificacion_limpieza: str,
        id_card_servicio: CardServicioVenta,
        id_turistas: Turista,
    ) -> CalificacionServicioUsuario:
        """
        Crea un registro de calificación.
        """

        return CalificacionServicioUsuario.objects.create(
            puntuacion_general=puntuacion_general,
            feedback_empresa=feedback_empresa,
            puntuacion_certificados=puntuacion_certificados,
            calificacion_puntualidad=calificacion_puntualidad,
            calificacion_limpieza=calificacion_limpieza,
            fecha_calificacion=timezone.now(),
            id_card_servicio=id_card_servicio,
            id_turistas=id_turistas,
        )

    @staticmethod
    def obtener_por_id(calificacion_id: int) -> Optional[CalificacionServicioUsuario]:
        """
        Obtiene una calificación por ID.
        """
        try:
            return CalificacionServicioUsuario.objects.get(id=calificacion_id)
        except CalificacionServicioUsuario.DoesNotExist:
            return None

    @staticmethod
    def actualizar_calificacion(calificacion: CalificacionServicioUsuario, **datos) -> CalificacionServicioUsuario:
        """
        Actualiza los campos de un registro de calificación.
        """
        for campo, valor in datos.items():
            setattr(calificacion, campo, valor)
        calificacion.save()
        return calificacion

    @staticmethod
    def eliminar_calificacion(calificacion_id: int) -> bool:
        """
        Elimina una calificación por ID.
        """
        calificacion = CalificacionRepository.obtener_por_id(calificacion_id)
        if calificacion:
            calificacion.delete()
            return True
        return False

    # -----------------------------
    # CONSULTAS PERSONALIZADAS
    # -----------------------------

    @staticmethod
    def obtener_por_turista(turista: Turista) -> QuerySet:
        """
        Retorna todas las calificaciones realizadas por un turista.
        """
        return CalificacionServicioUsuario.objects.filter(id_turistas=turista)

    @staticmethod
    def obtener_por_servicio(servicio: CardServicioVenta) -> QuerySet:
        """
        Retorna todas las calificaciones asociadas a un servicio.
        """
        return CalificacionServicioUsuario.objects.filter(id_card_servicio=servicio)

    @staticmethod
    def obtener_promedio_servicio(servicio: CardServicioVenta) -> float:
        """
        Calcula el promedio de calificación general para un servicio.
        """
        queryset = CalificacionServicioUsuario.objects.filter(id_card_servicio=servicio)

        if not queryset.exists():
            return 0.0

        promedio = queryset.aggregate(models.Avg("puntuacion_general"))["puntuacion_general__avg"]
        return float(promedio)

    @staticmethod
    def obtener_ultimas_calificaciones(limit=10) -> QuerySet:
        """
        Retorna las calificaciones más recientes.
        """
        return CalificacionServicioUsuario.objects.order_by("-fecha_calificacion")[:limit]
