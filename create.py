"""
Script para crear usuarios en WordPress mediante la API.

Requisitos:
- Tener instalado y activado el plugin REST API Key Authentication en WordPress.
- Configurar una clave de API en WordPress para autenticación.

Configuración:
- Modificar las variables wordpress_url, api_key, username, password y email según tus necesidades.

Ejemplo de uso:
1. Ejecutar el script para obtener un token de autenticación.
2. Utilizar el token para crear un nuevo usuario en WordPress.

Nota:
Asegúrate de que el usuario tenga los permisos necesarios para realizar operaciones a través de la API.

"""

import requests

# Configuración
wordpress_url = 'https://signifikativo.com.mx/wp-json/wp/v2/user_request'
api_key = 'TJ0e 27vh DD1K f8MS THSi tI1w'
username = 'prueba'
password = 'Titiapps321'
email = 'contacto@titi-apps.com'

# Obtener token de autenticación
auth_url = 'https://signifikativo.com.mx/wp-json/jwt-auth/v1/token'
auth_data = {
    'username': 'prueba',
    'password': 'Titiapps321',
}


auth_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Basic {api_key}',
}

auth_response = requests.post(auth_url, headers=auth_headers, json=auth_data)

if auth_response.status_code == 200:
    token = auth_response.json().get('token')
    print(f'Token de autenticación obtenido: {token}')

    # Crear usuario utilizando el token de autenticación
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    data = {
        'username': username,
        'password': password,
        'email': email,
    }

    response = requests.post(wordpress_url, headers=headers, json=data)

    if response.status_code == 201:
        print(f'Usuario {username} creado exitosamente.')
    else:
        print(f'Error al crear usuario. Código de estado: {response.status_code}, Mensaje: {response.text}')

else:
    print(f'Error al obtener el token. Código de estado: {auth_response.status_code}, Mensaje: {auth_response.text}')
