# LegalTurismoColombia

Plataforma para la verificación y promoción de servicios turísticos legales en Colombia.

## 📋 Descripción
Este proyecto busca fortalecer la legalidad en el turismo mediante la verificación de prestadores de servicios, uso de códigos QR para validación y un sistema de denuncias y calificaciones.

## 🚀 Guía de Instalación y Ejecución

### Prerrequisitos
- Python 3.8+
- Node.js y npm
- PostgreSQL

### 1. Configuración del Backend (Django)

1.  **Navegar a la carpeta del backend:**
    ```bash
    cd backend
    ```

2.  **Crear y activar el entorno virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    # O si no tienes el archivo aún:
    pip install django djangorestframework psycopg2-binary djangorestframework-simplejwt django-cors-headers python-dotenv
    ```

4.  **Configurar Variables de Entorno:**
    Crea un archivo `.env` en la carpeta `backend/` con lo siguiente (ajusta según tu BD):
    ```env
    DB_NAME=legalturismo_db
    DB_USER=postgres
    DB_PASSWORD=tu_contraseña
    DB_HOST=localhost
    DB_PORT=5432
    ```

5.  **Base de Datos:**
    Asegúrate de crear la base de datos en PostgreSQL:
    ```sql
    CREATE DATABASE legalturismo_db;
    ```

6.  **Migraciones y Superusuario:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser # Para acceder al admin
    ```

7.  **Ejecutar el servidor:**
    ```bash
    python manage.py runserver
    ```
    El backend correrá en `http://localhost:8000`.

### 2. Configuración del Frontend (React/Vite)

1.  **Navegar a la carpeta del frontend:**
    ```bash
    cd frontend
    ```

2.  **Instalar dependencias:**
    ```bash
    npm install
    ```

3.  **Ejecutar servidor de desarrollo:**
    ```bash
    npm run dev
    ```
    El frontend correrá generalmente en `http://localhost:5173`.

---

## 📂 Arquitectura del Backend

El backend está organizado en la carpeta `api/` siguiendo una estructura modular:

-   `api/models/`: Modelos de base de datos (Usuario, Prestador, Servicio, etc.).
-   `api/views/`: Lógica de los controladores (Vistas basadas en clases).
-   `api/serializers/`: Transformación de datos (Modelos <-> JSON).
-   `api/services/`: Lógica de negocio compleja (Filtros, QR).
-   `api/urls/`: Rutas de la API.

### 🗂️ Modelos de Base de Datos

| Modelo | Descripción |
| :--- | :--- |
| **Usuario** | Extiende de `AbstractUser`. Maneja autenticación, dirección y teléfono. |
| **Rol** | Roles del sistema (Turista, Prestador, Admin). Relación ManyToMany con Usuario. |
| **PrestadorServicio** | Perfil extendido para empresas. Contiene RNT, descripción y estado de validación. |
| **ServicioTuristico** | Servicios ofrecidos (Hoteles, Tours). Incluye precio, ciudad, categoría. |
| **Denuncia** | Reportes de usuarios sobre prestadores. Incluye evidencia y estado. |
| **Interaccion** | Registro de reservas/visitas reales. Necesario para poder calificar. |
| **Calificacion** | Puntuación (1-5) y comentarios. Requiere interacción previa. |

---

## 🔌 Documentación de la API

### Autenticación (JWT)
*Se debe configurar `simplejwt` en `urls.py` para obtener tokens.*
-   `POST /api/token/`: Obtener Access y Refresh Token.
-   `POST /api/token/refresh/`: Refrescar token.

### Prestadores
-   **Registro**: `POST /api/prestadores/registro/`
    -   Body: Datos del usuario y empresa.
    -   Acción: Crea usuario y perfil de prestador pendiente de validación.

### Servicios Turísticos
-   **Búsqueda**: `GET /api/servicios/buscar/`
    -   Params: `?categoria=Hotel&ciudad=Bogota&certificado=true`
    -   Respuesta: Lista de servicios filtrados.

### Denuncias
-   **Crear**: `POST /api/denuncias/crear/`
    -   Body: Motivo, descripción, evidencia (archivo).
    -   Requiere autenticación.

### Verificación QR
-   **Escanear**: `GET /api/qr/verificar/<codigo>/`
    -   Acción: Decodifica el QR y retorna la info pública del prestador para verificar su legalidad.

---

## 🤝 Pasos Siguientes para el Equipo

Para continuar el desarrollo y tener una versión presentable ("MVP"), sigan estos pasos:

1.  **Completar la Lógica de las Vistas (`api/views/`)**:
    -   Actualmente las vistas retornan respuestas simuladas. Deben conectar los `serializers` para guardar y leer datos reales de la BD.
    -   Ejemplo: En `RegistroPrestadorView`, usar `PrestadorServicioSerializer` para guardar los datos.

2.  **Implementar Autenticación JWT**:
    -   Agregar las rutas de `simplejwt` en `backend/urls.py`.
    -   Proteger las vistas que requieran login (como crear denuncia) usando `permission_classes = [IsAuthenticated]`.

3.  **Desarrollar el Servicio de QR (`api/services/qr_service.py`)**:
    -   Implementar la librería `qrcode` de Python para generar imágenes QR que apunten a la URL de validación del prestador.

4.  **Conectar Frontend con Backend**:
    -   Configurar `axios` o `fetch` en el frontend para consumir estos endpoints.
    -   Crear formularios para Registro y Búsqueda.

5.  **Poblar Base de Datos**:
    -   Crear un script o usar el Admin de Django (`/admin`) para crear roles, algunos usuarios y servicios de prueba.
