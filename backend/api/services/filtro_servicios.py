from api.models.servicio import ServicioTuristico

def filtrar_servicios(categoria=None, ciudad=None, certificado=None):
    """
    Filtra los servicios turísticos según los criterios.
    """
    queryset = ServicioTuristico.objects.all()
    
    if categoria:
        queryset = queryset.filter(categoria=categoria)
    
    if ciudad:
        queryset = queryset.filter(ciudad=ciudad)
        
    if certificado is not None:
        queryset = queryset.filter(certificado=certificado)
        
    return queryset
