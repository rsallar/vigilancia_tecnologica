"""
Módulo de generación de informes para el Asistente de Informes de Vigilancia Tecnológica.
Crea informes estructurados a partir de los resultados del análisis.
"""

import streamlit as st
import datetime
import pandas as pd

def generate_report(topic, scope, search_results, analysis_results):
    """
    Genera un informe estructurado de vigilancia tecnológica.
    
    Args:
        topic (str): Tema principal de la vigilancia tecnológica
        scope (dict): Diccionario con los parámetros del alcance
        search_results (pandas.DataFrame): Resultados de la búsqueda
        analysis_results (dict): Resultados del análisis
    
    Returns:
        dict: Diccionario con las secciones del informe
    """
    # Mostrar progreso de generación
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Inicializar diccionario para el informe
    report = {}
    
    # 1. Generar resumen ejecutivo (20%)
    status_text.text("Generando resumen ejecutivo...")
    progress_bar.progress(0.2)
    
    report['summary'] = generate_executive_summary(topic, scope, analysis_results)
    
    # 2. Generar metodología (40%)
    status_text.text("Documentando metodología...")
    progress_bar.progress(0.4)
    
    report['methodology'] = generate_methodology_section(scope)
    
    # 3. Generar análisis de resultados (60%)
    status_text.text("Elaborando análisis de resultados...")
    progress_bar.progress(0.6)
    
    report['analysis'] = generate_analysis_section(analysis_results)
    
    # 4. Generar conclusiones y recomendaciones (80%)
    status_text.text("Formulando conclusiones y recomendaciones...")
    progress_bar.progress(0.8)
    
    report['conclusions'] = generate_conclusions(topic, analysis_results)
    
    # 5. Finalizar estructura completa (100%)
    status_text.text("Finalizando informe...")
    progress_bar.progress(1.0)
    
    # Definir estructura completa del informe
    report['structure'] = [
        "1. Resumen Ejecutivo",
        "2. Introducción",
        "3. Metodología",
        "4. Análisis de Resultados",
        "   4.1. Evolución Temporal",
        "   4.2. Principales Actores",
        "   4.3. Tendencias Identificadas",
        "   4.4. Análisis por Fuentes",
        "5. Conclusiones y Recomendaciones",
        "6. Referencias",
        "7. Anexos"
    ]
    
    # Añadir metadatos
    report['metadata'] = {
        'title': f"Informe de Vigilancia Tecnológica: {topic}",
        'date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'author': "Generado con Asistente de Informes de Vigilancia Tecnológica",
        'version': "1.0"
    }
    
    # Limpiar elementos de progreso
    progress_bar.empty()
    status_text.empty()
    
    return report

def generate_executive_summary(topic, scope, analysis_results):
    """
    Genera el resumen ejecutivo del informe.
    
    Args:
        topic (str): Tema principal
        scope (dict): Parámetros del alcance
        analysis_results (dict): Resultados del análisis
    
    Returns:
        str: Texto del resumen ejecutivo
    """
    # Obtener información relevante
    trend = analysis_results['temporal']['trend']
    top_actors = list(analysis_results['actors'].keys())[:3]
    top_trends = sorted(analysis_results['trends'].items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Construir resumen
    summary = f"""
    ## Resumen Ejecutivo
    
    Este informe presenta los resultados de un proceso de vigilancia tecnológica sobre **{topic}**, 
    realizado durante el período {scope['time_period'].lower()}. El análisis revela una tendencia **{trend}** 
    en la producción de publicaciones relacionadas con esta temática.
    
    Los principales actores identificados en este campo son {', '.join(top_actors)}, 
    quienes lideran la investigación y desarrollo en diferentes aspectos de {topic}.
    
    Las tendencias más relevantes identificadas incluyen:
    """
    
    # Añadir lista de tendencias
    for trend, value in top_trends:
        summary += f"\n- **{trend}** (índice de relevancia: {value})"
    
    # Añadir conclusión
    summary += f"""
    
    Este informe proporciona una visión integral del estado actual y las tendencias emergentes en {topic},
    ofreciendo una base sólida para la toma de decisiones estratégicas y la identificación de oportunidades
    de innovación en este campo.
    """
    
    return summary

def generate_methodology_section(scope):
    """
    Genera la sección de metodología del informe.
    
    Args:
        scope (dict): Parámetros del alcance
    
    Returns:
        str: Texto de la sección de metodología
    """
    # Construir descripción de la metodología
    methodology = f"""
    ## Metodología
    
    La vigilancia tecnológica se realizó siguiendo un proceso sistemático de búsqueda, recopilación,
    análisis y difusión de información. El alcance del estudio se definió con los siguientes parámetros:
    
    - **Período de tiempo**: {scope['time_period']}
    - **Factores críticos monitoreados**:
    """
    
    # Añadir factores críticos
    factors = []
    if scope.get('monitor_tech_advances'):
        factors.append("Avances tecnológicos")
    if scope.get('monitor_market_trends'):
        factors.append("Tendencias de mercado")
    if scope.get('monitor_competitors'):
        factors.append("Competidores")
    if scope.get('monitor_regulations'):
        factors.append("Regulaciones y normativas")
    if scope.get('monitor_patents'):
        factors.append("Patentes y propiedad intelectual")
    if scope.get('monitor_research'):
        factors.append("Investigación académica")
    
    for factor in factors:
        methodology += f"\n  - {factor}"
    
    # Añadir palabras clave
    methodology += "\n\n- **Palabras clave utilizadas**:"
    for keyword in scope.get('keywords', []):
        methodology += f"\n  - {keyword}"
    
    # Añadir fuentes
    methodology += "\n\n- **Fuentes de información consultadas**:"
    sources = []
    if scope['sources'].get('scientific'):
        sources.append("Artículos científicos")
    if scope['sources'].get('patents'):
        sources.append("Patentes")
    if scope['sources'].get('news'):
        sources.append("Noticias especializadas")
    if scope['sources'].get('blogs'):
        sources.append("Blogs técnicos")
    if scope['sources'].get('social'):
        sources.append("Redes sociales")
    
    for source in sources:
        methodology += f"\n  - {source}"
    
    # Añadir descripción del proceso de análisis
    methodology += """
    
    El proceso de análisis incluyó las siguientes etapas:
    
    1. **Búsqueda y recopilación**: Identificación y extracción de información relevante de las fuentes seleccionadas.
    2. **Filtrado y clasificación**: Evaluación de la relevancia y calidad de la información recopilada.
    3. **Análisis cuantitativo**: Identificación de patrones, tendencias y relaciones mediante análisis estadístico.
    4. **Análisis cualitativo**: Interpretación contextual de los resultados y extracción de insights.
    5. **Síntesis y elaboración de conclusiones**: Integración de los hallazgos y formulación de recomendaciones.
    """
    
    return methodology

def generate_analysis_section(analysis_results):
    """
    Genera la sección de análisis de resultados del informe.
    
    Args:
        analysis_results (dict): Resultados del análisis
    
    Returns:
        str: Texto de la sección de análisis
    """
    # Construir sección de análisis
    analysis = """
    ## Análisis de Resultados
    
    ### Evolución Temporal
    
    El análisis de la evolución temporal de publicaciones muestra el siguiente patrón:
    """
    
    # Añadir datos de evolución temporal
    years = analysis_results['temporal']['publications_by_year']
    for year, count in sorted(years.items()):
        analysis += f"\n- **{year}**: {count} publicaciones"
    
    # Añadir tendencia
    analysis += f"\n\nEsto indica una tendencia **{analysis_results['temporal']['trend']}** en el interés por esta temática."
    
    # Añadir sección de actores principales
    analysis += """
    
    ### Principales Actores
    
    Los actores más relevantes en este campo, según el número de publicaciones y su relevancia, son:
    """
    
    # Añadir tabla de actores
    for actor, data in analysis_results['actors'].items():
        analysis += f"\n- **{actor}**: {data['Publicaciones']} publicaciones, índice de influencia {data['Índice de influencia']:.2f}"
    
    # Añadir sección de tendencias
    analysis += """
    
    ### Tendencias Identificadas
    
    El análisis de contenido ha permitido identificar las siguientes tendencias principales:
    """
    
    # Añadir tendencias ordenadas por relevancia
    for trend, value in sorted(analysis_results['trends'].items(), key=lambda x: x[1], reverse=True):
        analysis += f"\n- **{trend}**: índice de relevancia {value}"
    
    # Añadir sección de fuentes
    analysis += """
    
    ### Análisis por Fuentes
    
    La distribución de información por fuentes muestra el siguiente patrón:
    """
    
    # Añadir datos de fuentes
    sources = analysis_results['sources']['publications_by_source']
    relevance = analysis_results['sources']['relevance_by_source']
    
    for source, count in sorted(sources.items(), key=lambda x: x[1], reverse=True):
        analysis += f"\n- **{source}**: {count} publicaciones, relevancia media {relevance[source]:.2f}"
    
    return analysis

def generate_conclusions(topic, analysis_results):
    """
    Genera las conclusiones y recomendaciones del informe.
    
    Args:
        topic (str): Tema principal
        analysis_results (dict): Resultados del análisis
    
    Returns:
        str: Texto de las conclusiones
    """
    # Identificar tendencias principales
    top_trends = sorted(analysis_results['trends'].items(), key=lambda x: x[1], reverse=True)[:3]
    trend_names = [t[0] for t in top_trends]
    
    # Construir conclusiones
    conclusions = f"""
    ## Conclusiones y Recomendaciones
    
    ### Conclusiones Principales
    
    El análisis de vigilancia tecnológica sobre **{topic}** ha permitido identificar las siguientes conclusiones clave:
    
    1. La evolución temporal muestra una tendencia **{analysis_results['temporal']['trend']}**, lo que indica 
       {get_trend_interpretation(analysis_results['temporal']['trend'], topic)}.
    
    2. Los principales actores en este campo están enfocando sus esfuerzos en aspectos relacionados con 
       {', '.join(trend_names)}, lo que sugiere que estas áreas representan las líneas de desarrollo más prometedoras.
    
    3. La distribución de información por fuentes revela que {get_main_source(analysis_results['sources'])} 
       constituye la principal vía de difusión de avances en este campo, lo que destaca su importancia como 
       canal de comunicación para las innovaciones en {topic}.
    
    ### Recomendaciones
    
    Basándose en los hallazgos de este estudio, se proponen las siguientes recomendaciones:
    
    1. **Monitoreo continuo**: Establecer un sistema de vigilancia permanente sobre {trend_names[0]} y {trend_names[1]}, 
       dado su alto índice de relevancia y potencial impacto.
    
    2. **Colaboración estratégica**: Explorar posibilidades de colaboración con {list(analysis_results['actors'].keys())[0]} 
       y {list(analysis_results['actors'].keys())[1]}, considerando su posición de liderazgo en este campo.
    
    3. **Desarrollo de capacidades**: Fortalecer las competencias internas relacionadas con {trend_names[0]}, 
       para aprovechar esta tendencia emergente.
    
    4. **Vigilancia de competidores**: Prestar especial atención a las actividades de {list(analysis_results['actors'].keys())[2]}, 
       cuyo índice de influencia muestra un crecimiento significativo.
    
    5. **Diversificación de fuentes**: Ampliar el monitoreo para incluir {get_least_source(analysis_results['sources'])}, 
       que actualmente representa una fuente minoritaria pero podría ofrecer perspectivas complementarias valiosas.
    """
    
    return conclusions

def get_trend_interpretation(trend, topic):
    """Genera una interpretación de la tendencia temporal."""
    if trend == 'creciente':
        return f"un interés cada vez mayor en {topic} y sugiere un campo en expansión"
    else:
        return f"un campo dinámico con fluctuaciones en el interés por {topic}"

def get_main_source(sources_data):
    """Identifica la fuente principal según el número de publicaciones."""
    main_source = max(sources_data['publications_by_source'].items(), key=lambda x: x[1])
    return main_source[0]

def get_least_source(sources_data):
    """Identifica la fuente con menos publicaciones."""
    least_source = min(sources_data['publications_by_source'].items(), key=lambda x: x[1])
    return least_source[0]
