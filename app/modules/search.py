"""
Módulo de búsqueda para el Asistente de Informes de Vigilancia Tecnológica.
Gestiona la recopilación de información de diversas fuentes.
"""

import pandas as pd
import random
import time
import streamlit as st

def search_information(topic, scope):
    """
    Busca información relevante sobre el tema especificado según el alcance definido.
    
    Args:
        topic (str): Tema principal de la vigilancia tecnológica
        scope (dict): Diccionario con los parámetros del alcance
    
    Returns:
        pandas.DataFrame: DataFrame con los resultados de la búsqueda
    """
    # En un sistema real, aquí se implementaría la búsqueda en fuentes reales
    # Para este prototipo, generamos datos simulados
    
    # Mostrar progreso de búsqueda
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Simular búsqueda en diferentes fuentes
    sources = []
    if scope['sources']['scientific']:
        sources.append("Artículos científicos")
    if scope['sources']['patents']:
        sources.append("Patentes")
    if scope['sources']['news']:
        sources.append("Noticias especializadas")
    if scope['sources']['blogs']:
        sources.append("Blogs técnicos")
    if scope['sources']['social']:
        sources.append("Redes sociales")
    
    # Si no se seleccionó ninguna fuente, usar todas por defecto
    if not sources:
        sources = ["Artículos científicos", "Noticias especializadas", "Blogs técnicos"]
    
    # Crear lista para almacenar resultados
    results = []
    
    # Simular búsqueda en cada fuente
    for i, source in enumerate(sources):
        # Actualizar progreso
        progress = (i + 1) / len(sources)
        progress_bar.progress(progress)
        status_text.text(f"Buscando en {source}...")
        
        # Simular tiempo de búsqueda
        time.sleep(0.5)
        
        # Generar resultados simulados para esta fuente
        source_results = generate_simulated_results(topic, scope, source)
        results.extend(source_results)
    
    # Limpiar elementos de progreso
    progress_bar.empty()
    status_text.empty()
    
    # Convertir resultados a DataFrame
    df = pd.DataFrame(results)
    
    return df

def generate_simulated_results(topic, scope, source):
    """
    Genera resultados simulados para una fuente específica.
    
    Args:
        topic (str): Tema principal
        scope (dict): Parámetros del alcance
        source (str): Fuente de información
    
    Returns:
        list: Lista de diccionarios con resultados simulados
    """
    # Número de resultados a generar
    num_results = random.randint(5, 15)
    
    # Palabras clave del tema
    keywords = scope.get('keywords', [])
    if not keywords:
        keywords = [topic]
    
    # Años para las fechas
    years = []
    if scope['time_period'] == "Últimos 6 meses":
        years = [2025]
    elif scope['time_period'] == "Último año":
        years = [2024, 2025]
    elif scope['time_period'] == "Últimos 2 años":
        years = [2023, 2024, 2025]
    elif scope['time_period'] == "Últimos 5 años":
        years = [2020, 2021, 2022, 2023, 2024, 2025]
    else:
        years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    
    # Posibles autores/organizaciones
    authors = [
        "Universidad de Stanford", "MIT", "Google Research", "OpenAI", 
        "Microsoft Research", "IBM", "Meta AI", "DeepMind", "Amazon",
        "Universidad de Berkeley", "ETH Zurich", "Tsinghua University",
        "NVIDIA Research", "Apple", "Samsung Research", "Baidu Research"
    ]
    
    # Posibles títulos según la fuente
    title_prefixes = {
        "Artículos científicos": [
            "Avances en", "Un estudio sobre", "Análisis de", "Investigación de",
            "Nuevos enfoques para", "Metodología para", "Evaluación de"
        ],
        "Patentes": [
            "Sistema y método para", "Dispositivo para", "Método de", 
            "Aparato para", "Proceso de", "Tecnología de"
        ],
        "Noticias especializadas": [
            "Cómo", "Por qué", "El futuro de", "La revolución de",
            "Tendencias en", "El impacto de", "Novedades en"
        ],
        "Blogs técnicos": [
            "Guía de", "Tutorial de", "Implementando", "Explorando",
            "Comparativa de", "Optimizando", "Soluciones para"
        ],
        "Redes sociales": [
            "Opinión sobre", "Debate sobre", "Tendencia:", "Viral:",
            "Discusión:", "Actualización de", "Lanzamiento de"
        ]
    }
    
    # Generar resultados
    results = []
    for i in range(num_results):
        # Seleccionar aleatoriamente elementos para este resultado
        year = random.choice(years)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        date = f"{year}-{month:02d}-{day:02d}"
        
        author = random.choice(authors)
        keyword = random.choice(keywords)
        prefix = random.choice(title_prefixes.get(source, ["Sobre"]))
        
        # Crear título
        title = f"{prefix} {keyword} en el contexto de {topic}"
        
        # Relevancia (1-10)
        relevance = random.randint(5, 10)
        
        # URL simulada
        if source == "Artículos científicos":
            url = f"https://journal.science/{year}/{month}/article{i}.html"
        elif source == "Patentes":
            url = f"https://patents.org/{year}/{i:05d}"
        elif source == "Noticias especializadas":
            url = f"https://technews.com/{year}/{month}/{day}/news{i}.html"
        elif source == "Blogs técnicos":
            url = f"https://techblog.com/posts/{year}/{i:04d}"
        else:
            url = f"https://social.net/post/{i:06d}"
        
        # Añadir resultado
        results.append({
            "Título": title,
            "Autor/Organización": author,
            "Fecha": date,
            "Fuente": source,
            "Relevancia": relevance,
            "URL": url
        })
    
    return results
