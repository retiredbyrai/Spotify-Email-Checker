# Spotify Email Checker

Spotify Email Checker es una herramienta para validar cuentas de correo electrónico registradas en Spotify. Proporciona opciones para importar cuentas, configurar proxies, ajustar el número de hilos y guardar resultados de las validaciones.

## Características
- Importar un archivo de cuentas en formato `email:contraseña`.
- Verificar si un correo electrónico está registrado en Spotify.
- Soporte para proxies (HTTP, HTTPS, SOCKS4, SOCKS5).
- Configuración del número de hilos para optimizar la validación.
- Exportar resultados de validación a un archivo.

## Propósito
Esta herramienta es solo para propósitos educacionales. No debe ser utilizada para actividades malintencionadas ni para violar los términos de servicio de Spotify o cualquier otra plataforma.

## Requisitos
- Python 3.8 o superior.
- Librerías requeridas (se instalan mediante `requirements.txt`):
  - `requests`
  - `colorama`

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/SpotifyEmailChecker.git
   cd SpotifyEmailChecker
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
Ejecuta el archivo principal:
```bash
python src/account_validator.py
```
Sigue las opciones del menú para:
- Importar cuentas.
- Validar cuentas.
- Configurar proxies.
- Exportar resultados.

### Formato del archivo de cuentas
El archivo debe tener el siguiente formato:
```
email1@example.com:contraseña1
email2@example.com:contraseña2
```

### Formato del archivo de proxies
El archivo debe listar las proxies en el siguiente formato:
```
proxy1:puerto
proxy2:puerto
```

## Opciones del Menú
1. **Importar Cuentas**: Proporciona la ruta de un archivo con las cuentas a validar.
2. **Validar Cuentas**: Inicia el proceso de validación y guarda los resultados.
3. **Activar/Desactivar Proxies**: Alterna el uso de proxies durante la validación.
4. **Configurar Número de Hilos**: Ajusta el número de hilos para optimizar el rendimiento.
5. **Importar Proxies**: Carga un archivo de proxies.
6. **Elegir Tipo de Proxy**: Configura el tipo de proxy (HTTP, HTTPS, SOCKS4, SOCKS5).
7. **Salir**: Cierra la aplicación.

## Resultados
Los resultados se guardan automáticamente en un archivo dentro de la carpeta `results/` con un nombre basado en la fecha y hora:
```
results-YYYY-MM-DD_HH-MM-SS.txt
```

## Contribuciones
Si deseas contribuir, realiza un fork del repositorio, crea una rama para tus cambios y envía un pull request. Asegúrate de seguir las mejores prácticas de código y agregar documentación si es necesario.

## Licencia
Este proyecto está bajo la licencia [MIT](LICENSE).

---

¡Gracias por usar Spotify Email Checker! Si tienes preguntas o sugerencias, no dudes en abrir un issue.

