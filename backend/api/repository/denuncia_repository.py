from typing import Optional
from django.db.models import QuerySet
from django.utils import timezone

from ..models.denuncia import RegistroReporte
from ..models.prestador_individual import PrestadorIndividual
from ..models.empresas_prestadoras import EmpresaPrestadora
from ..models.turista import Turista


class RegistroReporteRepository:
    """
    Capa de acceso a datos para RegistroReporte.
    Encapsula todas las operaciones CRUD + consultas comunes.
    """

    # -------------------------------------------------------------------
    # CRUD BÁSICO
    # -------------------------------------------------------------------

    @staticmethod
    def crear_reporte(
        tipo_reporte: str,
        descripcion_detallada: str,
        id_turista: Optional[Turista] = None,
        id_prestador_individual_reportado: Optional[PrestadorIndividual] = None,
        id_empresas_prestadoras: Optional[EmpresaPrestadora] = None,
        url_evidencia_adjunta: Optional[str] = None,
    ) -> RegistroReporte:
        """
        Crea un nuevo reporte. El estado por defecto es 'ABIERTO'.
        """

        return RegistroReporte.objects.create(
            fecha_hora_reporte=timezone.now(),
            tipo_reporte=tipo_reporte,
            descripcion_detallada=descripcion_detallada,
            url_evidencia_adjunta=url_evidencia_adjunta,
            estado_gestion=RegistroReporte.EstadoGestion.ABIERTO,
            id_prestador_individual_reportado=id_prestador_individual_reportado,
            id_empresas_prestadoras=id_empresas_prestadoras,
            id_turista=id_turista,
        )

    @staticmethod
    def obtener_por_id(reporte_id: int) -> Optional[RegistroReporte]:
        """
        Devuelve un reporte por ID o None si no existe.
        """
        try:
            return RegistroReporte.objects.get(id=reporte_id)
        except RegistroReporte.DoesNotExist:
            return None

    @staticmethod
    def actualizar_reporte(reporte: RegistroReporte, **datos) -> RegistroReporte:
        """
        Actualiza campos del reporte.
        """
        for campo, valor in datos.items():
            setattr(reporte, campo, valor)
        reporte.save()
        return reporte

    @staticmethod
    def eliminar_reporte(reporte_id: int) -> bool:
        """
        Elimina un reporte por ID.
        """
        reporte = RegistroReporteRepository.obtener_por_id(reporte_id)
        if reporte:
            reporte.delete()
            return True
        return False

    # -------------------------------------------------------------------
    # CONSULTAS PERSONALIZADAS
    # -------------------------------------------------------------------

    @staticmethod
    def obtener_por_turista(turista: Turista) -> QuerySet:
        """
        Reportes realizados por un turista específico.
        """
        return RegistroReporte.objects.filter(id_turista=turista)

    @staticmethod
    def obtener_por_prestador_individual(prestador: PrestadorIndividual) -> QuerySet:
        """
        Reportes hechos contra un prestador individual.
        """
        return RegistroReporte.objects.filter(id_prestador_individual_reportado=prestador)

    @staticmethod
    def obtener_por_empresa(empresa: EmpresaPrestadora) -> QuerySet:
        """
        Reportes hechos contra una empresa prestadora.
        """
        return RegistroReporte.objects.filter(id_empresas_prestadoras=empresa)

    @staticmethod
    def obtener_abiertos() -> QuerySet:
        """
        Lista de reportes en estado ABIERTO.
        """
        return RegistroReporte.objects.filter(
            estado_gestion=RegistroReporte.EstadoGestion.ABIERTO
        )

    @staticmethod
    def obtener_en_proceso() -> QuerySet:
        """
        Lista de reportes en estado EN_PROCESO.
        """
        return RegistroReporte.objects.filter(
            estado_gestion=RegistroReporte.EstadoGestion.EN_PROCESO
        )

    @staticmethod
    def obtener_cerrados() -> QuerySet:
        """
        Lista de reportes CERRADOS.
        """
        return RegistroReporte.objects.filter(
            estado_gestion=RegistroReporte.EstadoGestion.CERRADO
        )

    @staticmethod
    def cerrar_reporte(reporte: RegistroReporte, gestion: str) -> RegistroReporte:
        """
        Cambia el estado de un reporte a CERRADO y registra fecha + gestión.
        """
        reporte.estado_gestion = RegistroReporte.EstadoGestion.CERRADO
        reporte.fecha_cierre_gestion = timezone.now()
        reporte.gestion_tomada = gestion
        reporte.save()
        return reporte

    @staticmethod
    def obtener_recientes(limit: int = 10) -> QuerySet:
        """
        Últimos N reportes creados.
        """
        return RegistroReporte.objects.order_by("-fecha_hora_reporte")[:limit]
