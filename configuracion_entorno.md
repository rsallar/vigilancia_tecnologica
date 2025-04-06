# Configuración del Entorno de Despliegue

## Repositorio Git Local

He configurado un repositorio Git local para la aplicación "Asistente para Informes de Vigilancia Tecnológica" con la siguiente estructura:

```
vigilancia_tecnologica_repo/
├── .streamlit/
│   ├── config.toml        # Configuración del tema visual
│   └── secrets.toml       # Configuración del servidor
├── app/
│   ├── main.py            # Aplicación principal
│   ├── modules/           # Módulos funcionales
│   ├── templates/         # Plantillas para informes
│   └── utils/             # Utilidades
├── data/                  # Datos y recursos
├── Home.py                # Página de inicio
├── README.md              # Documentación principal
├── requirements.txt       # Dependencias
└── [Documentación adicional]
```

Todos los archivos necesarios han sido añadidos al repositorio y se ha realizado un commit inicial.

## Preparación para Streamlit Cloud

Para completar el despliegue en Streamlit Cloud, necesitamos:

1. **Crear un repositorio en GitHub**: Esto permitirá a Streamlit Cloud acceder al código.
2. **Vincular el repositorio local con GitHub**: Para subir el código al repositorio remoto.
3. **Configurar la aplicación en Streamlit Cloud**: Conectando con el repositorio de GitHub.

## Pasos para el Despliegue

1. Crear un repositorio en GitHub llamado "vigilancia-tecnologica"
2. Conectar el repositorio local con el remoto:
   ```
   git remote add origin https://github.com/[usuario]/vigilancia-tecnologica.git
   git push -u origin master
   ```
3. Acceder a Streamlit Cloud (https://streamlit.io/cloud)
4. Crear una nueva aplicación vinculada al repositorio de GitHub
5. Configurar los parámetros de despliegue:
   - Archivo principal: Home.py
   - Python version: 3.10
   - Dependencias: requirements.txt

## Consideraciones Adicionales

- **Permisos**: El repositorio debe ser público para usar la versión gratuita de Streamlit Cloud
- **Actualizaciones**: Cualquier cambio en el repositorio de GitHub se reflejará automáticamente en la aplicación desplegada
- **Dominio**: Streamlit Cloud proporcionará un subdominio en streamlit.app
- **Recursos**: La versión gratuita tiene limitaciones de recursos, pero son suficientes para esta aplicación educativa

La configuración del entorno está completa y lista para proceder con el despliegue de la aplicación en Streamlit Cloud.
