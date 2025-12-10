# Django setup removed for shell execution
from api.models import Usuario, EmpresaPrestadora, CardServicioVenta
from api.models.prestador_individual import PrestadorIndividual

try:
    print("--- DEBUG START ---")
    u = Usuario.objects.get(id=3)
    print(f"User found: {u.email} (ID: {u.id})")
    
    empresa = EmpresaPrestadora.objects.filter(usuario=u).first()
    individual = PrestadorIndividual.objects.filter(usuario=u).first()
    
    if empresa:
        print(f"User is Empresa: {empresa.nombre_razon_social} (ID: {empresa.id_empresa})")
        servicios = CardServicioVenta.objects.filter(empresa_prestadora=empresa)
        print(f"Services linked to Empresa: {servicios.count()}")
        for s in servicios:
            print(f" - {s.titulo_card} (ID: {s.id})")
            
    if individual:
        print(f"User is Individual Provider: {individual.nombre} (ID: {individual.id_prestador})")
        servicios = CardServicioVenta.objects.filter(prestador_individual=individual)
        print(f"Services linked to Individual: {servicios.count()}")
        for s in servicios:
            print(f" - {s.titulo_card} (ID: {s.id})")

    if not empresa and not individual:
        print("User is NOT linked to any provider (Empresa or Individual).")

except Usuario.DoesNotExist:
    print("User with ID 3 not found.")
except Exception as e:
    print(f"Error: {e}")
print("--- DEBUG END ---")
