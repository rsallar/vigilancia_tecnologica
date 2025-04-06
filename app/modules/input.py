"""
Módulo de entrada para el Asistente de Informes de Vigilancia Tecnológica.
Gestiona la recopilación de información inicial del usuario.
"""

import streamlit as st
import datetime

def get_user_input():
    """
    Recopila la información inicial del usuario para definir el alcance de la vigilancia tecnológica.
    
    Returns:
        tuple: (topic, scope) donde topic es el tema principal y scope es un diccionario con los parámetros del alcance
    """
    st.subheader("Definición del alcance de la vigilancia tecnológica")
    
    # Tema principal
    topic = st.text_input("Tema principal de la vigilancia tecnológica", 
                         placeholder="Ej: Inteligencia Artificial Generativa")
    
    # Contenedor para los parámetros del alcance
    scope = {}
    
    # Período de tiempo
    st.markdown("### Período de tiempo")
    time_options = ["Últimos 6 meses", "Último año", "Últimos 2 años", "Últimos 5 años", "Sin restricción"]
    scope['time_period'] = st.selectbox("Selecciona el período de tiempo", time_options)
    
    # Factores críticos de vigilancia
    st.markdown("### Factores críticos de vigilancia")
    st.markdown("Selecciona los factores que deseas monitorear:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        scope['monitor_tech_advances'] = st.checkbox("Avances tecnológicos", value=True)
        scope['monitor_market_trends'] = st.checkbox("Tendencias de mercado", value=True)
        scope['monitor_competitors'] = st.checkbox("Competidores", value=True)
    
    with col2:
        scope['monitor_regulations'] = st.checkbox("Regulaciones y normativas", value=False)
        scope['monitor_patents'] = st.checkbox("Patentes y propiedad intelectual", value=False)
        scope['monitor_research'] = st.checkbox("Investigación académica", value=True)
    
    # Palabras clave
    st.markdown("### Palabras clave")
    keywords = st.text_area("Introduce palabras clave relevantes (una por línea)", 
                           placeholder="Ej:\nInteligencia Artificial\nDeep Learning\nGeneración de contenido")
    
    if keywords:
        scope['keywords'] = [kw.strip() for kw in keywords.split('\n') if kw.strip()]
    else:
        scope['keywords'] = []
    
    # Fuentes de información
    st.markdown("### Fuentes de información")
    
    scope['sources'] = {}
    scope['sources']['scientific'] = st.checkbox("Artículos científicos", value=True)
    scope['sources']['patents'] = st.checkbox("Patentes", value=False)
    scope['sources']['news'] = st.checkbox("Noticias especializadas", value=True)
    scope['sources']['blogs'] = st.checkbox("Blogs técnicos", value=True)
    scope['sources']['social'] = st.checkbox("Redes sociales", value=False)
    
    # Información adicional
    st.markdown("### Información adicional")
    scope['additional_info'] = st.text_area("Información adicional o contexto relevante", 
                                          placeholder="Proporciona cualquier información adicional que pueda ser útil...")
    
    # Fecha de creación
    scope['creation_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return topic, scope
