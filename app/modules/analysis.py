"""
Módulo de análisis para el Asistente de Informes de Vigilancia Tecnológica.
Procesa y analiza la información recopilada para extraer insights relevantes.
"""

import pandas as pd
import numpy as np
import streamlit as st
from collections import Counter

def analyze_data(search_results):
    """
    Analiza los resultados de la búsqueda para extraer tendencias, actores principales y otros insights.
    
    Args:
        search_results (pandas.DataFrame): DataFrame con los resultados de la búsqueda
    
    Returns:
        dict: Diccionario con los resultados del análisis
    """
    # Mostrar progreso de análisis
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Inicializar diccionario para resultados
    analysis_results = {}
    
    # 1. Análisis temporal (25%)
    status_text.text("Analizando evolución temporal...")
    progress_bar.progress(0.25)
    
    # Convertir columna de fecha a datetime
    search_results['Fecha'] = pd.to_datetime(search_results['Fecha'])
    
    # Agrupar por año y mes
    search_results['Año'] = search_results['Fecha'].dt.year
    search_results['Mes'] = search_results['Fecha'].dt.month
    
    # Contar publicaciones por año
    publications_by_year = search_results.groupby('Año').size()
    
    # Guardar en resultados
    analysis_results['temporal'] = {
        'publications_by_year': publications_by_year.to_dict(),
        'trend': 'creciente' if publications_by_year.is_monotonic_increasing else 'variable'
    }
    
    # 2. Análisis de fuentes (50%)
    status_text.text("Analizando fuentes de información...")
    progress_bar.progress(0.5)
    
    # Contar publicaciones por fuente
    publications_by_source = search_results.groupby('Fuente').size()
    
    # Calcular relevancia promedio por fuente
    relevance_by_source = search_results.groupby('Fuente')['Relevancia'].mean()
    
    # Guardar en resultados
    analysis_results['sources'] = {
        'publications_by_source': publications_by_source.to_dict(),
        'relevance_by_source': relevance_by_source.to_dict()
    }
    
    # 3. Análisis de actores (75%)
    status_text.text("Identificando actores principales...")
    progress_bar.progress(0.75)
    
    # Contar publicaciones por autor/organización
    publications_by_actor = search_results.groupby('Autor/Organización').size()
    
    # Calcular relevancia promedio por actor
    relevance_by_actor = search_results.groupby('Autor/Organización')['Relevancia'].mean()
    
    # Crear DataFrame de actores
    actors_df = pd.DataFrame({
        'Publicaciones': publications_by_actor,
        'Relevancia promedio': relevance_by_actor
    }).sort_values(by=['Publicaciones', 'Relevancia promedio'], ascending=False)
    
    # Calcular índice de influencia (fórmula simple)
    actors_df['Índice de influencia'] = actors_df['Publicaciones'] * actors_df['Relevancia promedio'] / 10
    
    # Guardar en resultados
    analysis_results['actors'] = actors_df.head(10).to_dict('index')
    
    # 4. Análisis de tendencias (100%)
    status_text.text("Identificando tendencias principales...")
    progress_bar.progress(1.0)
    
    # Simular identificación de tendencias basadas en títulos
    # En un sistema real, esto utilizaría NLP más avanzado
    trends = {
        'Innovación': np.random.randint(60, 100),
        'Aplicaciones': np.random.randint(50, 90),
        'Investigación': np.random.randint(40, 80),
        'Desarrollo': np.random.randint(30, 70),
        'Regulación': np.random.randint(20, 60),
        'Mercado': np.random.randint(30, 80),
        'Competencia': np.random.randint(20, 70)
    }
    
    # Guardar en resultados
    analysis_results['trends'] = trends
    
    # Limpiar elementos de progreso
    progress_bar.empty()
    status_text.empty()
    
    return analysis_results
