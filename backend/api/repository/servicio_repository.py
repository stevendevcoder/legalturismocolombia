from django.core.exceptions import ObjectDoesNotExist
from ..models.servicio import CardServicioVenta


class CardServicioVentaRepository:

    # ---------------------------- CREAR ----------------------------
    def create(
        self,
        titulo_card,
        descripcion_corta,
        url_imagen_principal,
        unidad_precio,
        nombre_servicio,
        estado_publicacion,
        categoria_servicio,
        id_registro_propina=None
    ):
        card = CardServicioVenta.objects.create(
            titulo_card=titulo_card,
            descripcion_corta=descripcion_corta,
            url_imagen_principal=url_imagen_principal,
            unidad_precio=unidad_precio,
            nombre_servicio=nombre_servicio,
            estado_publicacion=estado_publicacion,
            categoria_servicio=categoria_servicio,
            id_registro_propina=id_registro_propina
        )
        return card

    # ---------------------------- OBTENER ----------------------------
    def get_by_id(self, card_id):
        try:
            return CardServicioVenta.objects.get(id=card_id)
        except ObjectDoesNotExist:
            return None

    def get_all(self):
        return CardServicioVenta.objects.all()

    # ---------------------------- ACTUALIZAR ----------------------------
    def update(self, card_id, **kwargs):
        try:
            card = CardServicioVenta.objects.get(id=card_id)
            for key, value in kwargs.items():
                setattr(card, key, value)
            card.save()
            return card
        except ObjectDoesNotExist:
            return None

    # ---------------------------- ELIMINAR ----------------------------
    def delete(self, card_id):
        try:
            card = CardServicioVenta.objects.get(id=card_id)
            card.delete()
            return True
        except ObjectDoesNotExist:
            return False

    # ---------------------------- CONSULTAS EXTRA ----------------------------

    def get_publicados(self):
        """Devuelve solo los cards publicados."""
        return CardServicioVenta.objects.filter(estado_publicacion=True)

    def get_no_publicados(self):
        """Devuelve solo los cards NO publicados."""
        return CardServicioVenta.objects.filter(estado_publicacion=False)

    def get_by_categoria(self, categoria):
        """Filtra por categoría del servicio."""
        return CardServicioVenta.objects.filter(categoria_servicio=categoria)

    def search_by_nombre(self, texto):
        """Búsqueda por coincidencia parcial en el nombre del servicio."""
        return CardServicioVenta.objects.filter(nombre_servicio__icontains=texto)

    def search_by_titulo(self, texto):
        """Búsqueda por coincidencia parcial en el título del card."""
        return CardServicioVenta.objects.filter(titulo_card__icontains=texto)

    def get_by_propina(self, propina_id):
        """Devuelve todos los cards asociados a un registro de propina."""
        return CardServicioVenta.objects.filter(id_registro_propina__id=propina_id)
