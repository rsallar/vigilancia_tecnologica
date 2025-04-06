import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Añadir directorios al path para importar módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'templates'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

# Importar módulos de la aplicación
from modules.input import get_user_input
from modules.search import search_information
from modules.analysis import analyze_data
from modules.report import generate_report
from modules.review import review_report

# Configuración de la página
st.set_page_config(
    page_title="Asistente para Informes de Vigilancia Tecnológica",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título y descripción
st.title("Asistente para Informes de Vigilancia Tecnológica")
st.markdown("""
Este asistente te guiará en la creación de informes profesionales de vigilancia tecnológica, 
ayudándote a recopilar, analizar y presentar información relevante sobre tendencias tecnológicas.
""")

# Añadir información sobre el proyecto
st.sidebar.markdown("## Sobre este proyecto")
st.sidebar.info(
    "Esta aplicación fue desarrollada como un caso de uso de Manus "
    "para la asignatura de Vigilancia Tecnológica. Permite a los estudiantes "
    "aprender y aplicar metodologías de vigilancia tecnológica de manera práctica."
)

# Inicializar variables de estado de la sesión
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'topic' not in st.session_state:
    st.session_state.topic = ""
if 'search_results' not in st.session_state:
    st.session_state.search_results = None
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'report' not in st.session_state:
    st.session_state.report = None

# Barra lateral con pasos del proceso
st.sidebar.title("Proceso de Vigilancia Tecnológica")
st.sidebar.markdown("### Pasos:")
steps = [
    "1. Definición del alcance",
    "2. Búsqueda de información",
    "3. Análisis de datos",
    "4. Generación del informe",
    "5. Revisión y mejora"
]

for i, step in enumerate(steps, 1):
    if i < st.session_state.step:
        st.sidebar.success(step)
    elif i == st.session_state.step:
        st.sidebar.info(step)
    else:
        st.sidebar.markdown(step)

# Contenido principal según el paso actual
if st.session_state.step == 1:
    st.session_state.topic, st.session_state.scope = get_user_input()
    if st.button("Continuar a búsqueda de información"):
        st.session_state.step = 2
        st.experimental_rerun()

elif st.session_state.step == 2:
    st.subheader(f"Búsqueda de información sobre: {st.session_state.topic}")
    
    with st.spinner("Buscando información relevante..."):
        st.session_state.search_results = search_information(st.session_state.topic, st.session_state.scope)
    
    st.success("Búsqueda completada")
    st.dataframe(st.session_state.search_results)
    
    if st.button("Continuar al análisis de datos"):
        st.session_state.step = 3
        st.experimental_rerun()

elif st.session_state.step == 3:
    st.subheader("Análisis de datos")
    
    with st.spinner("Analizando información..."):
        st.session_state.analysis_results = analyze_data(st.session_state.search_results)
    
    # Mostrar algunos resultados del análisis
    st.success("Análisis completado")
    
    # Visualización de tendencias
    st.subheader("Tendencias identificadas")
    fig, ax = plt.subplots(figsize=(10, 6))
    trends = st.session_state.analysis_results['trends']
    ax.bar(trends.keys(), trends.values())
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Relevancia')
    ax.set_title('Tendencias principales identificadas')
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Actores principales
    st.subheader("Actores principales")
    st.dataframe(st.session_state.analysis_results['actors'])
    
    if st.button("Continuar a la generación del informe"):
        st.session_state.step = 4
        st.experimental_rerun()

elif st.session_state.step == 4:
    st.subheader("Generación del informe")
    
    with st.spinner("Generando informe..."):
        st.session_state.report = generate_report(
            topic=st.session_state.topic,
            scope=st.session_state.scope,
            search_results=st.session_state.search_results,
            analysis_results=st.session_state.analysis_results
        )
    
    st.success("Informe generado correctamente")
    
    # Mostrar vista previa del informe
    st.subheader("Vista previa del informe")
    st.markdown(st.session_state.report['summary'])
    
    # Mostrar estructura del informe
    st.subheader("Estructura del informe")
    for section in st.session_state.report['structure']:
        st.markdown(f"- **{section}**")
    
    if st.button("Continuar a revisión y mejora"):
        st.session_state.step = 5
        st.experimental_rerun()

elif st.session_state.step == 5:
    st.subheader("Revisión y mejora del informe")
    
    with st.spinner("Revisando informe..."):
        review_results = review_report(st.session_state.report)
    
    st.success("Revisión completada")
    
    # Mostrar sugerencias de mejora
    st.subheader("Sugerencias de mejora")
    for suggestion in review_results['suggestions']:
        st.markdown(f"- {suggestion}")
    
    # Opciones para exportar
    st.subheader("Exportar informe")
    export_format = st.selectbox("Selecciona formato de exportación", ["PDF", "HTML", "DOCX"])
    
    if st.button(f"Exportar como {export_format}"):
        st.success(f"Informe exportado como {export_format}")
        # Aquí se implementaría la funcionalidad real de exportación
    
    # Opción para reiniciar el proceso
    if st.button("Iniciar nuevo informe"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.experimental_rerun()

# Pie de página
st.markdown("---")
st.markdown("Desarrollado como caso de uso de Manus para la asignatura de Vigilancia Tecnológica")
st.markdown("© 2025 - Todos los derechos reservados")
