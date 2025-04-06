# Asistente para Informes de Vigilancia Tecnológica

Esta aplicación web guía a los estudiantes a través del proceso completo de vigilancia tecnológica, desde la definición del alcance hasta la generación y revisión de informes profesionales.

## Características

- **Definición del alcance**: Especificación del tema, período de tiempo, factores críticos y fuentes de información
- **Búsqueda de información**: Recopilación automática de datos de múltiples fuentes
- **Análisis de datos**: Identificación de tendencias, actores principales y patrones relevantes
- **Generación de informes**: Creación de informes estructurados con visualizaciones
- **Revisión y mejora**: Evaluación del informe y sugerencias de optimización

## Instalación local

1. Clonar el repositorio:
```
git clone https://github.com/usuario/vigilancia_tecnologica.git
cd vigilancia_tecnologica
```

2. Instalar dependencias:
```
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```
streamlit run app/main.py
```

## Estructura del proyecto

```
vigilancia_tecnologica/
├── app/
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── modules/
│   │   ├── input.py           # Módulo de entrada
│   │   ├── search.py          # Módulo de búsqueda
│   │   ├── analysis.py        # Módulo de análisis
│   │   ├── report.py          # Módulo de generación de informes
│   │   └── review.py          # Módulo de revisión
│   ├── templates/             # Plantillas para informes
│   └── utils/                 # Utilidades para procesamiento de datos
├── data/
│   ├── sources/               # Fuentes de datos predefinidas
│   └── cache/                 # Caché de búsquedas
├── .streamlit/
│   └── config.toml            # Configuración de Streamlit
└── requirements.txt           # Dependencias del proyecto
```

## Uso

1. **Definición del alcance**:
   - Introduce el tema principal
   - Selecciona el período de tiempo
   - Marca los factores críticos relevantes
   - Añade palabras clave
   - Selecciona fuentes de información

2. **Búsqueda de información**:
   - Revisa los resultados de la búsqueda
   - Filtra si es necesario
   - Continúa al análisis

3. **Análisis de datos**:
   - Explora las visualizaciones generadas
   - Revisa tendencias identificadas
   - Examina actores principales
   - Continúa a la generación del informe

4. **Generación del informe**:
   - Revisa la vista previa del informe
   - Verifica la estructura
   - Continúa a la revisión

5. **Revisión y mejora**:
   - Revisa sugerencias de mejora
   - Selecciona formato de exportación
   - Exporta el informe final

## Valor educativo

Esta herramienta permite a los estudiantes:
- Aprender metodologías de vigilancia tecnológica de manera práctica
- Desarrollar habilidades de análisis e interpretación de datos
- Crear informes profesionales con estructura adecuada
- Comprender la importancia de la vigilancia tecnológica en entornos reales

## Desarrollado por

Este proyecto fue desarrollado como un caso de uso de Manus para la asignatura de Vigilancia Tecnológica.

© 2025 - Todos los derechos reservados
