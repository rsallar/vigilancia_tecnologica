"""
Módulo de revisión para el Asistente de Informes de Vigilancia Tecnológica.
Evalúa y sugiere mejoras para los informes generados.
"""

import streamlit as st
import random

def review_report(report):
    """
    Revisa el informe generado y sugiere mejoras.
    
    Args:
        report (dict): Diccionario con las secciones del informe
    
    Returns:
        dict: Diccionario con los resultados de la revisión
    """
    # Mostrar progreso de revisión
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Inicializar diccionario para resultados de la revisión
    review_results = {
        'score': 0,
        'suggestions': [],
        'strengths': []
    }
    
    # 1. Revisar estructura (25%)
    status_text.text("Revisando estructura del informe...")
    progress_bar.progress(0.25)
    
    # Verificar que todas las secciones estén presentes
    required_sections = ['summary', 'methodology', 'analysis', 'conclusions']
    missing_sections = [section for section in required_sections if section not in report]
    
    if missing_sections:
        for section in missing_sections:
            review_results['suggestions'].append(f"Añadir la sección de {section} al informe.")
    else:
        review_results['strengths'].append("El informe tiene una estructura completa con todas las secciones necesarias.")
    
    # 2. Revisar contenido (50%)
    status_text.text("Revisando contenido del informe...")
    progress_bar.progress(0.5)
    
    # Simular revisión de contenido
    # En un sistema real, esto utilizaría NLP más avanzado
    
    # Revisar resumen ejecutivo
    if 'summary' in report and len(report['summary']) < 200:
        review_results['suggestions'].append("Ampliar el resumen ejecutivo para incluir más detalles sobre los hallazgos principales.")
    else:
        review_results['strengths'].append("El resumen ejecutivo es completo y proporciona una buena visión general del informe.")
    
    # Revisar metodología
    if 'methodology' in report:
        review_results['strengths'].append("La sección de metodología está bien documentada.")
    
    # Revisar análisis
    if 'analysis' in report:
        # Sugerir mejoras aleatorias para el análisis
        possible_suggestions = [
            "Incluir más visualizaciones para representar las tendencias identificadas.",
            "Profundizar en el análisis de los actores principales, incluyendo sus áreas de especialización.",
            "Añadir un análisis comparativo con períodos anteriores para identificar cambios en las tendencias.",
            "Incluir un análisis de correlación entre diferentes tendencias identificadas.",
            "Considerar añadir un análisis geográfico de la distribución de publicaciones."
        ]
        
        # Seleccionar 2 sugerencias aleatorias
        selected_suggestions = random.sample(possible_suggestions, 2)
        review_results['suggestions'].extend(selected_suggestions)
    
    # Revisar conclusiones
    if 'conclusions' in report:
        review_results['strengths'].append("Las conclusiones están bien fundamentadas en los resultados del análisis.")
        
        # Sugerir mejora aleatoria para las conclusiones
        possible_suggestions = [
            "Ampliar las recomendaciones con acciones más específicas.",
            "Incluir un cronograma sugerido para la implementación de las recomendaciones.",
            "Añadir una sección de limitaciones del estudio para contextualizar las conclusiones."
        ]
        
        selected_suggestion = random.choice(possible_suggestions)
        review_results['suggestions'].append(selected_suggestion)
    
    # 3. Revisar formato y presentación (75%)
    status_text.text("Revisando formato y presentación...")
    progress_bar.progress(0.75)
    
    # Sugerir mejoras de formato
    review_results['suggestions'].append("Considerar añadir un índice de contenidos al inicio del informe.")
    review_results['suggestions'].append("Incluir encabezados y pies de página con la información del informe.")
    
    # 4. Calcular puntuación general (100%)
    status_text.text("Calculando puntuación general...")
    progress_bar.progress(1.0)
    
    # Calcular puntuación basada en fortalezas y sugerencias
    base_score = 7.0  # Puntuación base
    strength_bonus = len(review_results['strengths']) * 0.5  # Bonificación por fortalezas
    suggestion_penalty = len(review_results['suggestions']) * 0.2  # Penalización por sugerencias
    
    # Calcular puntuación final (escala 1-10)
    final_score = min(10, max(1, base_score + strength_bonus - suggestion_penalty))
    review_results['score'] = round(final_score, 1)
    
    # Añadir evaluación general
    if final_score >= 9:
        review_results['overall'] = "Excelente informe, con estructura clara y análisis profundo."
    elif final_score >= 7:
        review_results['overall'] = "Buen informe, con algunas áreas de mejora menores."
    elif final_score >= 5:
        review_results['overall'] = "Informe aceptable, pero requiere mejoras significativas."
    else:
        review_results['overall'] = "El informe necesita una revisión sustancial."
    
    # Limpiar elementos de progreso
    progress_bar.empty()
    status_text.empty()
    
    return review_results
