#!/bin/bash
# Script to create GitHub issues for Voice Agent project
# Usage: ./create-issues.sh

# Verificar que gh está instalado
if ! command -v gh &> /dev/null; then
    echo "GitHub CLI (gh) no está instalado. Instálalo desde https://cli.github.com"
    exit 1
fi

# Array de issues
declare -a ISSUES=(
    "Audio Input Module - Micrófono|Implementar el módulo completo de captura de audio del micrófono con soporte para múltiples dispositivos y manejo robusto de errores.|audio,core,enhancement"
    "Audio Output Module - Altavoz|Implementar el módulo de reproducción de audio por altavoz con control de volumen y sincronización.|audio,core,enhancement"
    "Speech-to-Text Integration|Implementar la integración con OpenAI Whisper para transcripción de audio a texto.|stt,core,api-integration"
    "LLM Integration - OpenAI|Implementar la integración con OpenAI para generar respuestas conversacionales.|llm,core,api-integration"
    "Text-to-Speech Integration|Implementar Text-to-Speech usando pyttsx3 como solución offline-first.|tts,core,audio"
    "Agent Core Loop - Orquestación|Implementar el loop principal del agente que orquesta todos los componentes en tiempo real.|core,asyncio,architecture"
    "Configuration Management|Mejorar el sistema de configuración para soportar múltiples entornos y providers.|configuration,enhancement"
    "Testing Suite|Crear suite completa de tests unitarios e integración.|testing,quality"
    "Documentation|Crear documentación completa del proyecto.|documentation"
    "Voice Activity Detection (VAD)|Implementar detección automática de actividad de voz para mejorar la experiencia.|enhancement,audio"
)

echo "Creando issues en GitHub..."

for issue in "${ISSUES[@]}"; do
    IFS='|' read -r title body labels <<< "$issue"
    
    echo "Creando: $title"
    
    gh issue create \
        --title "$title" \
        --body "$body" \
        --label "$labels" \
        2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo "✓ $title creado exitosamente"
    else
        echo "✗ Error creando $title"
    fi
    
    # Pequeña pausa entre requests
    sleep 1
done

echo "¡Proceso completado!"
