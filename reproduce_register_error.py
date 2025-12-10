import requests
import json
import random

url = "http://localhost:8000/api/auth/register/"
rnd = random.randint(1000, 9999)

# Datos de prueba para EMPRESA
payload = {
    # Datos generales
    "nombre": f"TestMultipart_{rnd}",
    "apellido": "UserMulti",
    "email": f"testmultipart_{rnd}@example.com",
    "password": "password123",
    "nombre_tipo": "EMPRESA",
    "fecha_nacimiento": "1990-01-01",
    "numero_telefonico": "3007654321",
    "tipo_identificacion": "CC",
    "num_identificacion": f"9988{rnd}",
    
    # Campos planos de empresa
    "nit_empresa": f"900{rnd}",
    "nombre_razon_social": f"Empresa Multipart SAS {rnd}",
    "direccion": "Avenida Siempre Viva 123",
    "categoria_empresa": "Tours",
    "rnt_empresa": f"11{rnd}",
    "matricula_mercantil": f"33{rnd}",
}

# Sending as multipart/form-data (using 'files' kwarg with explicit None for unused files)
# Typically requests sends multipart if 'files' is present.
# We can submit mixed data/files.
files = {
    'dummy_file': (None, ''), # Trick to force multipart without real files
}

try:
    # ... (Register request above)
    response = requests.post(url, data=payload, files=files)
    
    print(f"Register Status: {response.status_code}")
    data = response.json()
    
    if response.status_code == 201:
        access_token = data['tokens']['access']
        print(f"\nTesting Protected Endpoint with Token: {access_token[:15]}...")
        
        # Test Protected Endpoint
        profile_url = "http://localhost:8000/api/users/profile/"
        headers = {'Authorization': f'Bearer {access_token}'}
        
        # UserProfile now accepts GET
        profile_response = requests.get(profile_url, headers=headers)
        print(f"Profile Status: {profile_response.status_code}")
        print(profile_response.text)
    else:
        print(json.dumps(data, indent=2))

except Exception as e:
    print(f"Error: {e}")
