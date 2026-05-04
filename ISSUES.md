# GitHub Issues - Voice Agent Project

Los siguientes issues han sido creados para rastrear el progreso del proyecto Voice Agent.
Para crear los issues en GitHub, puedes usar la interfaz web o la CLI de GitHub.

## Issue #1: Audio Input Module - Micrófono
**Prioridad**: Alta  
**Etiquetas**: `audio`, `core`, `enhancement`

### Descripción
Implementar el módulo completo de captura de audio del micrófono con soporte para múltiples dispositivos y manejo robusto de errores.

### Requisitos
- [x] Clase `Microphone` base (estructura)
- [ ] Implementación de inicio/parada de grabación
- [ ] Lectura de chunks de audio en asyncio
- [ ] Detección automática de dispositivo de entrada
- [ ] Manejo de cambios en dispositivos durante ejecución
- [ ] Validación de parámetros de audio
- [ ] Tests unitarios
- [ ] Documentación

### Criterios de Aceptación
- Captura audio a 16kHz, 16-bit PCM
- Latencia < 100ms entre captura y disponibilidad del dato
- Sin interrupciones durante grabación

---

## Issue #2: Audio Output Module - Altavoz
**Prioridad**: Alta  
**Etiquetas**: `audio`, `core`, `enhancement`

### Descripción
Implementar el módulo de reproducción de audio por altavoz con control de volumen y sincronización.

### Requisitos
- [x] Clase `Speaker` base (estructura)
- [ ] Implementación de reproducción de audio
- [ ] Control de volumen en rango 0.0-1.0
- [ ] Manejo de dispositivos múltiples
- [ ] Buffer para reproducción suave
- [ ] Sincronización con el pipeline
- [ ] Tests unitarios
- [ ] Documentación

### Criterios de Aceptación
- Reproducción sin interrupciones
- Control de volumen funcional
- Sincronización con generación de audio

---

## Issue #3: Speech-to-Text Integration
**Prioridad**: Alta  
**Etiquetas**: `stt`, `core`, `api-integration`

### Descripción
Implementar la integración con OpenAI Whisper para transcripción de audio a texto.

### Requisitos
- [x] Clase `STTProvider` base
- [x] Estructura de `WhisperSTT`
- [ ] Implementación real de transcripción con Whisper
- [ ] Soporte para múltiples idiomas
- [ ] Caché de resultados
- [ ] Manejo de errores de API
- [ ] Retry logic con backoff
- [ ] Tests con mocks
- [ ] Documentación

### Criterios de Aceptación
- Precisión > 90%
- Latencia < 2 segundos
- Soporte bilingüe (español/inglés)

---

## Issue #4: LLM Integration - OpenAI
**Prioridad**: Alta  
**Etiquetas**: `llm`, `core`, `api-integration`

### Descripción
Implementar la integración con OpenAI para generar respuestas conversacionales.

### Requisitos
- [x] Clase `LLMProvider` base
- [x] Estructura de `OpenAILLM`
- [ ] Implementación real de generación con GPT
- [ ] Soporte para system prompts personalizados
- [ ] Manejo de contexto conversacional
- [ ] Retry logic y rate limiting
- [ ] Validación de respuestas
- [ ] Tests con mocks
- [ ] Documentación

### Criterios de Aceptación
- Respuestas coherentes y contextualizadas
- Soporte para system prompts
- Manejo de errores de rate limiting

---

## Issue #5: Text-to-Speech Integration
**Prioridad**: Alta  
**Etiquetas**: `tts`, `core`, `audio`

### Descripción
Implementar Text-to-Speech usando pyttsx3 (sin API) como solución offline-first.

### Requisitos
- [x] Clase `TTSProvider` base
- [x] Estructura de `Pyttsx3TTS`
- [ ] Implementación real de síntesis con pyttsx3
- [ ] Control de velocidad (TTS_RATE)
- [ ] Control de volumen
- [ ] Soporte para múltiples voces
- [ ] Conversión a array NumPy
- [ ] Tests
- [ ] Documentación

### Criterios de Aceptación
- Voz natural y legible
- Latencia < 1 segundo por oración
- Funciona offline

---

## Issue #6: Agent Core Loop - Orquestación
**Prioridad**: Alta  
**Etiquetas**: `core`, `asyncio`, `architecture`

### Descripción
Implementar el loop principal del agente que orquesta todos los componentes en tiempo real.

### Requisitos
- [x] Estructura básica de `VoiceAgent`
- [ ] Inicialización y cleanup de componentes
- [ ] Loop principal no-bloqueante
- [ ] State machine completamente funcional
- [ ] Gestión de timeouts
- [ ] Manejo de errores robusto
- [ ] Logging comprehensivo
- [ ] Tests de integración
- [ ] Documentación

### Criterios de Aceptación
- Latencia end-to-end < 5 segundos
- Operaciones completamente asincrónicas
- State transitions correctas

---

## Issue #7: Configuration Management
**Prioridad**: Media  
**Etiquetas**: `configuration`, `enhancement`

### Descripción
Mejorar el sistema de configuración para soportar múltiples entornos y providers.

### Requisitos
- [x] Sistema de `.env` con validación
- [ ] Soporte para múltiples profiles (dev, prod, test)
- [ ] Validación de tipos para config
- [ ] Documentación de todas las opciones
- [ ] Ejemplos de configuración
- [ ] Defaults sensatos

### Criterios de Aceptación
- Fácil cambio entre providers
- Configuración escalable
- Validación robusta

---

## Issue #8: Testing Suite
**Prioridad**: Media  
**Etiquetas**: `testing`, `quality`

### Descripción
Crear suite completa de tests unitarios e integración.

### Requisitos
- [ ] Tests unitarios para cada componente
- [ ] Tests de integración del pipeline
- [ ] Mocks para APIs externas
- [ ] Fixtures reutilizables
- [ ] Coverage report
- [ ] CI/CD configuration

### Criterios de Aceptación
- Coverage > 80%
- Todos los tests pasan
- Tests ejecutables con pytest

---

## Issue #9: Documentation
**Prioridad**: Media  
**Etiquetas**: `documentation`

### Descripción
Crear documentación completa del proyecto.

### Requisitos
- [x] README.md profesional
- [x] CLIENT_BRIEF.md
- [x] docs/architecture.md
- [x] docs/setup.md
- [x] docs/api.md
- [ ] Ejemplos de uso completos
- [ ] Troubleshooting guide
- [ ] Contributing guide

### Criterios de Aceptación
- Documentación clara y completa
- Ejemplos funcionales
- Fácil onboarding para nuevos desarrolladores

---

## Issue #10: Voice Activity Detection (VAD)
**Prioridad**: Baja  
**Etiquetas**: `enhancement`, `audio`

### Descripción
Implementar detección automática de actividad de voz para mejorar la experiencia.

### Requisitos
- [ ] Implementación de VAD simple
- [ ] Configuración de sensibilidad
- [ ] Integración con microphone module
- [ ] Tests

### Criterios de Aceptación
- Detecta correctamente inicio y fin de habla
- Mejora la experiencia del usuario

---

## Issue #11: Multi-turn Context
**Prioridad**: Baja  
**Etiquetas**: `enhancement`, `llm`

### Descripción
Mejorar el manejo de contexto conversacional para mantener conversaciones más naturales.

### Requisitos
- [ ] State machine mejorada para contexto
- [ ] Historia de conversación persistente
- [ ] Ventana de contexto configurable
- [ ] Tests

---

## Issue #12: Error Recovery
**Prioridad**: Media  
**Etiquetas**: `reliability`, `core`

### Descripción
Implementar recuperación robusta de errores en el pipeline.

### Requisitos
- [ ] Retry logic para operaciones fallidas
- [ ] Fallback providers
- [ ] Recuperación de estado
- [ ] User feedback mejorado

### Criterios de Aceptación
- Recuperación automática de fallos temporales
- User experience no se degrada significativamente

---

## Instrucciones para Crear los Issues en GitHub

### Opción 1: CLI de GitHub (gh)
```bash
# Instalar GitHub CLI si no lo tienes
# Luego, para cada issue:
gh issue create --title "Issue Title" --body "Issue Description" --label "label1,label2"
```

### Opción 2: Interfaz Web
1. Ir a https://github.com/tu-usuario/voice_agent/issues
2. Click en "New issue"
3. Copiar el título y descripción
4. Crear el issue

### Opción 3: Script Automatizado
Ver `.github/create-issues.sh` para script de automatización.

---

**Última actualización**: Mayo 2026
**Total de issues**: 12
**Prioridad**: 7 Alta, 3 Media, 2 Baja
