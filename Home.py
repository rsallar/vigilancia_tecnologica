import streamlit as st

st.set_page_config(
    page_title="Vigilancia Tecnológica - Inicio",
    page_icon="📊",
    layout="wide"
)

st.title("Bienvenido al Asistente para Informes de Vigilancia Tecnológica")

st.markdown("""
## Una herramienta educativa para la asignatura de Vigilancia Tecnológica

Esta aplicación web guía a los estudiantes a través del proceso completo de vigilancia tecnológica, 
desde la definición del alcance hasta la generación y revisión de informes profesionales.

### ¿Qué es la Vigilancia Tecnológica?

La vigilancia tecnológica es un proceso sistemático de captura, análisis y difusión de información 
sobre avances científicos y tecnológicos, que permite a las organizaciones tomar decisiones con menor 
riesgo y anticiparse a los cambios.

### ¿Qué puedes hacer con esta herramienta?

- Definir el alcance de tu vigilancia tecnológica
- Buscar información relevante en múltiples fuentes
- Analizar datos para identificar tendencias y actores clave
- Generar informes profesionales estructurados
- Recibir sugerencias para mejorar tus informes
""")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    ### Para estudiantes
    
    Esta herramienta te ayudará a:
    - Aprender metodologías de vigilancia tecnológica de manera práctica
    - Desarrollar habilidades de análisis e interpretación de datos
    - Crear informes profesionales con estructura adecuada
    - Comprender la importancia de la vigilancia tecnológica en entornos reales
    """)

with col2:
    st.success("""
    ### Para profesores
    
    Esta herramienta te permite:
    - Demostrar procesos de vigilancia tecnológica en clase
    - Asignar proyectos prácticos a los estudiantes
    - Evaluar la capacidad de análisis y síntesis
    - Proporcionar una experiencia de aprendizaje significativa
    """)

st.markdown("---")

st.header("Comenzar a utilizar la herramienta")

if st.button("Iniciar Asistente para Informes de Vigilancia Tecnológica", type="primary"):
    st.switch_page("app/main.py")

st.markdown("---")
st.markdown("Desarrollado como caso de uso de Manus para la asignatura de Vigilancia Tecnológica")
st.markdown("© 2025 - Todos los derechos reservados")
