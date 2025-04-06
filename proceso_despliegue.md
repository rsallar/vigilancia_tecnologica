# Proceso de Despliegue en Streamlit Cloud

## 1. Creación del Repositorio en GitHub

Para desplegar nuestra aplicación en Streamlit Cloud, primero necesitamos crear un repositorio en GitHub:

1. Acceder a GitHub (https://github.com)
2. Crear un nuevo repositorio público llamado "vigilancia-tecnologica"
3. Inicializar sin README ni .gitignore (ya que tenemos nuestro repositorio local)

## 2. Vinculación del Repositorio Local con GitHub

Una vez creado el repositorio en GitHub, vinculamos nuestro repositorio local:

```bash
git remote add origin https://github.com/[usuario]/vigilancia-tecnologica.git
git push -u origin master
```

Esto subirá todo nuestro código al repositorio de GitHub, incluyendo:
- La aplicación principal (Home.py)
- Los módulos funcionales en la carpeta app/
- La configuración de Streamlit en .streamlit/
- La documentación y archivos de requisitos

## 3. Configuración en Streamlit Cloud

Con el código en GitHub, procedemos a configurar el despliegue en Streamlit Cloud:

1. Acceder a Streamlit Cloud (https://streamlit.io/cloud)
2. Iniciar sesión o crear una cuenta
3. Hacer clic en "New app"
4. Seleccionar el repositorio "vigilancia-tecnologica"
5. Configurar los parámetros de despliegue:
   - Archivo principal: Home.py
   - Rama: master
   - Python version: 3.10
   - Paquetes: requirements.txt (ya incluido en el repositorio)
6. Hacer clic en "Deploy"

## 4. Proceso de Despliegue

Una vez configurado, Streamlit Cloud:
1. Clona el repositorio de GitHub
2. Crea un entorno virtual con las dependencias especificadas
3. Ejecuta la aplicación Streamlit
4. Asigna una URL permanente con el formato: https://[usuario]-vigilancia-tecnologica.streamlit.app

El proceso de despliegue puede tomar unos minutos mientras Streamlit Cloud instala todas las dependencias y configura el entorno.

## 5. URL de la Aplicación

Una vez completado el despliegue, la aplicación estará disponible en:
```
https://[usuario]-vigilancia-tecnologica.streamlit.app
```

Esta URL es permanente y puede ser compartida con los estudiantes para acceder a la herramienta desde cualquier lugar y en cualquier momento.

## 6. Actualizaciones Futuras

Para actualizar la aplicación en el futuro:
1. Realizar cambios en el repositorio local
2. Hacer commit de los cambios: `git commit -am "Descripción de los cambios"`
3. Subir los cambios a GitHub: `git push origin master`
4. Streamlit Cloud detectará automáticamente los cambios y actualizará la aplicación

Este proceso de actualización permite mantener la aplicación al día sin necesidad de volver a configurar el despliegue.
