# Wp_create_user
Crear usuario nuevo en WP con Python

Para obtener los permisos necesarios para interactuar con la API de WordPress, generalmente necesitas utilizar un token de autenticación. Aquí hay una guía básica de cómo puedes obtener esos permisos:

# Instala y activa el plugin de REST API Key Authentication:
- Ve al panel de administración de WordPress.
- Navega a "Plugins" y haz clic en "Añadir nuevo".
- Busca "REST API Key Authentication" e instálalo y actívalo.
# Genera una clave de API:
- Después de activar el plugin, ve a "Usuarios" -> "Claves de la aplicación" en el panel de administración.
- Haz clic en "Añadir nueva" para generar una nueva clave de API.
- Asigna los permisos adecuados según tus necesidades.
# Obtén el token de autenticación:
- Utiliza las credenciales del usuario (nombre de usuario y contraseña) junto con la clave de API para obtener un token de autenticación.
