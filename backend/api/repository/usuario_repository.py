from api.models.usuario import Usuario

class UsuarioRepo:
    @staticmethod
    def create_user(password, **data):
        """
        Crea un usuario usando el manager personalizado de Usuario.
        """
        return Usuario.objects.create_user(password=password, **data)

    @staticmethod
    def get_by_email(email):
        try:
            return Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return None
    
    @staticmethod
    def get_by_id(user_id):
        return Usuario.objects.get(id=user_id)

    @staticmethod
    def update(usuario, data):
        """
        Recibe una instancia de usuario y un diccionario de datos.
        Actualiza los campos y guarda en base de datos.
        """
        for key, value in data.items():
            
            setattr(usuario, key, value)
        
        usuario.save()
        return usuario
