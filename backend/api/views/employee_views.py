from rest_framework import viewsets, permissions
from rest_framework.response import Response
from api.models.empleados_registrados import EmpleadoRegistrado
from api.models.empresas_prestadoras import EmpresaPrestadora
from api.serializers.employee_serializers import EmpleadoRegistradoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoRegistrado.objects.all()
    serializer_class = EmpleadoRegistradoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = EmpleadoRegistrado.objects.filter(is_active=True)
        
        # Filter by current user's company
        mine = self.request.query_params.get('mine', None)
        if mine == 'true' and self.request.user.is_authenticated:
            user = self.request.user
            empresa = EmpresaPrestadora.objects.filter(usuario=user).first()
            
            if empresa:
                queryset = queryset.filter(nit_empresa_fk=empresa)
            else:
                queryset = queryset.none()
        
        return queryset

    def perform_create(self, serializer):
        # Assign company based on logged in user
        user = self.request.user
        empresa = EmpresaPrestadora.objects.filter(usuario=user).first()
        
        if empresa:
            serializer.save(nit_empresa_fk=empresa)
        else:
            # Handle case where user is not a company
            raise PermissionError("Solo empresas pueden registrar empleados")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=204)
