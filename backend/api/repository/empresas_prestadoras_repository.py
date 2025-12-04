from django.core.exceptions import ObjectDoesNotExist
from ..models.empresas_prestadoras import EmpresaPrestadora


class EmpresaPrestadoraRepository:

    # ---------------------------- CREAR ----------------------------
    def create(
        self,
        nit_empresa,
        nombre_razon_social,
        direccion,
        categoria_empresa,
        rnt_empresa,
        url_rnt_certificado,
        matricula_mercantil,
        url_cert_camara_comercio,
        id_usuario,
        id_cardServicioVenta=None,
        id_certificadosHabilidades=None
    ):
        empresa = EmpresaPrestadora.objects.create(
            nit_empresa=nit_empresa,
            nombre_razon_social=nombre_razon_social,
            direccion=direccion,
            categoria_empresa=categoria_empresa,
            rnt_empresa=rnt_empresa,
            url_rnt_certificado=url_rnt_certificado,
            matricula_mercantil=matricula_mercantil,
            url_cert_camara_comercio=url_cert_camara_comercio,
            id_usuario=id_usuario,
            id_cardServicioVenta=id_cardServicioVenta,
            id_certificadosHabilidades=id_certificadosHabilidades
        )
        return empresa

    # ---------------------------- OBTENER ----------------------------
    def get_by_nit(self, nit_empresa):
        try:
            return EmpresaPrestadora.objects.get(nit_empresa=nit_empresa)
        except ObjectDoesNotExist:
            return None

    def get_all(self):
        return EmpresaPrestadora.objects.all()

    # ---------------------------- ACTUALIZAR ----------------------------
    def update(self, nit_empresa, **kwargs):
        try:
            empresa = EmpresaPrestadora.objects.get(nit_empresa=nit_empresa)
            for key, value in kwargs.items():
                setattr(empresa, key, value)
            empresa.save()
            return empresa
        except ObjectDoesNotExist:
            return None

    # ---------------------------- ELIMINAR ----------------------------
    def delete(self, nit_empresa):
        """
        Retorna:
        - True si se eliminó
        - False si no existe
        """
        try:
            empresa = EmpresaPrestadora.objects.get(nit_empresa=nit_empresa)
            empresa.delete()
            return True
        except ObjectDoesNotExist:
            return False

    # ---------------------------- CONSULTAS EXTRA ----------------------------
    def get_by_rnt(self, rnt_empresa):
        """Busca empresa por su número RNT (único)."""
        try:
            return EmpresaPrestadora.objects.get(rnt_empresa=rnt_empresa)
        except ObjectDoesNotExist:
            return None

    def get_by_categoria(self, categoria):
        """Retorna empresas filtradas por categoría."""
        return EmpresaPrestadora.objects.filter(categoria_empresa=categoria)

    def get_by_usuario(self, usuario_id):
        """Retorna empresas asociadas a un usuario (representante legal)."""
        return EmpresaPrestadora.objects.filter(id_usuario__id=usuario_id)
