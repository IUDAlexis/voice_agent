# CLIENT BRIEF - Voice Agent

## 📋 Información General del Proyecto

**Nombre del Proyecto**: Voice Agent - Agente de Voz Conversacional  
**Fecha de Elaboración**: Mayo 2026  
**Tipo de Proyecto**: Educativo / Investigación  
**Objetivo de Aprendizaje**: Comprender la arquitectura de sistemas de voz conversacional en tiempo real

---

## 🎯 Objetivo Principal

Construir un **agente de voz conversacional mínimo en Python puro** que funcione en tiempo real, utilizando `asyncio` como base para:

1. Comprender profundamente cómo funcionan frameworks como Pipecat y LiveKit Agents
2. Implementar un loop en tiempo real sin dependencias externas complejas
3. Integrar componentes de audio, STT, LLM y TTS en un flujo coherente

---

## 🏗️ Arquitectura del Sistema

### Flujo Principal: Pipeline de Voz

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌──────────────┐
│  Micrófono  │────▶│     STT     │────▶│     LLM     │────▶│     TTS     │────▶│   Altavoz    │
│  (Audio In) │     │ (Whisper)   │     │  (Claude)   │     │ (pyttsx3)   │     │  (Audio Out) │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘     └──────────────┘
      ▲                                                                                  │
      │                                                                                  │
      └──────────────────────────────────────────────────────────────────────────────────┘
                           Loop Asincrónico (asyncio)
```

### Componentes Principales

| Componente | Responsabilidad | Entrada | Salida |
|-----------|-----------------|---------|--------|
| **Audio Input** | Capturar audio del micrófono | Micrófono | Audio RAW |
| **STT (Speech-to-Text)** | Convertir audio en texto | Audio RAW | Texto |
| **LLM (Language Model)** | Procesar texto y generar respuesta | Texto | Texto de respuesta |
| **TTS (Text-to-Speech)** | Convertir texto a audio | Texto | Audio WAV |
| **Audio Output** | Reproducir audio en altavoz | Audio WAV | Sonido |
| **Orchestrator** | Coordinar todo el pipeline | Señales de control | Estado del sistema |

---

## 💡 Requisitos Funcionales

### RF1: Captura de Audio en Tiempo Real
- **Descripción**: El sistema debe capturar audio del micrófono continuamente
- **Criterio de aceptación**: 
  - Audio capturado a 16kHz, 16-bit mono
  - Latencia < 100ms
  - Sin interrupciones en la captura

### RF2: Speech-to-Text (STT)
- **Descripción**: Convertir audio a texto usando OpenAI Whisper o similar
- **Criterio de aceptación**:
  - Precisión > 90% en español/inglés
  - Latencia de procesamiento < 2 segundos
  - Manejo de múltiples idiomas

### RF3: Integración con LLM
- **Descripción**: Procesar texto con un modelo de lenguaje
- **Criterio de aceptación**:
  - Integración con OpenAI API o local (Ollama)
  - Respuestas coherentes y contextualizadas
  - Soporte para system prompts personalizados

### RF4: Text-to-Speech (TTS)
- **Descripción**: Convertir texto de respuesta a audio
- **Criterio de aceptación**:
  - Voz natural y legible
  - Latencia < 1 segundo por oración
  - Soporte para múltiples voces y velocidades

### RF5: Reproducción de Audio
- **Descripción**: Reproducir el audio generado en el altavoz
- **Criterio de aceptación**:
  - Reproducción sin interrupciones
  - Control de volumen
  - Sincronización con el pipeline

### RF6: Loop Asincrónico en Tiempo Real
- **Descripción**: Orquestar todos los componentes usando asyncio
- **Criterio de aceptación**:
  - Latencia total end-to-end < 5 segundos
  - Operaciones no-bloqueantes
  - Manejo de errores robusto

---

## 🔧 Requisitos No-Funcionales

| Requisito | Descripción |
|-----------|------------|
| **Código Puro** | Python sin dependencias externas complejas (máximo librerías estándar + audio) |
| **Async-First** | Uso de `asyncio` como base del diseño |
| **Modular** | Componentes desacoplados y reutilizables |
| **Documentado** | Código comentado y documentación clara |
| **Testeable** | Componentes con tests unitarios |
| **Educational** | Código educativo y fácil de entender |
| **Performance** | Latencia mínima, optimizado para tiempo real |

---

## 🛠️ Stack Tecnológico

### Core
- **Python 3.10+**: Lenguaje principal
- **asyncio**: Loop asincrónico en tiempo real
- **typing**: Type hints para mejor código

### Audio
- **PyAudio**: Captura/reproducción de audio
- **SoundFile**: Lectura/escritura de archivos de audio
- **NumPy**: Procesamiento de arrays de audio

### APIs Externas
- **OpenAI Whisper** o **OpenAI API**: STT
- **OpenAI API** o **Claude API**: LLM
- **pyttsx3**: TTS local (offline-first)

### Desarrollo
- **pytest**: Testing
- **black**: Code formatting
- **mypy**: Type checking
- **python-dotenv**: Variables de entorno

---

## 📊 Fases del Proyecto

### Fase 1: Setup y Estructura (Semana 1)
- [x] Crear repositorio GitHub
- [x] Definir estructura del proyecto
- [x] Crear Client Brief y README
- [ ] Implementar estructura de directorios
- [ ] Crear configuración base

### Fase 2: Módulos Base (Semana 2)
- [ ] Implementar módulo de audio (micrófono)
- [ ] Crear clase base para STT
- [ ] Crear clase base para LLM
- [ ] Crear clase base para TTS

### Fase 3: Integraciones (Semana 3)
- [ ] Integrar Whisper para STT
- [ ] Integrar Claude/OpenAI para LLM
- [ ] Integrar pyttsx3 para TTS
- [ ] Tests unitarios para cada componente

### Fase 4: Orquestación (Semana 4)
- [ ] Implementar loop principal asincrónico
- [ ] Integrar todos los componentes
- [ ] Manejo de errores y edge cases
- [ ] Tests de integración

### Fase 5: Validación y Deployment (Semana 5)
- [ ] Tests end-to-end
- [ ] Documentación completa
- [ ] Ejemplos de uso
- [ ] Guía de instalación

---

## 🎓 Conceptos a Aprender

1. **Asyncio en Python**: Conceptos de coroutines, tasks, y event loops
2. **Procesamiento de Audio**: Captura y reproducción de audio en tiempo real
3. **Integración de APIs**: Uso de APIs externas en un flujo asincrónico
4. **Patrones de Diseño**: Clases base, inyección de dependencias, factory pattern
5. **Arquitectura de Sistemas**: Pipeline design, buffering, sincronización
6. **Testing**: Unit tests y integration tests para sistemas complejos

---

## 💾 Dependencias Principales

```
# Core
asyncio (stdlib)
typing (stdlib)

# Audio
PyAudio==0.2.13
SoundFile==0.12.1
NumPy==1.24.0

# APIs
openai==0.28.0
python-dotenv==1.0.0

# TTS
pyttsx3==2.90

# Dev
pytest==7.4.0
black==23.7.0
mypy==1.4.1
```

---

## 📈 Métricas de Éxito

- [x] Repositorio GitHub con estructura clara
- [x] README y Client Brief completos
- [ ] Todos los componentes implementados
- [ ] Tests con cobertura > 80%
- [ ] Latencia end-to-end < 5 segundos
- [ ] Código documentado y tipo-safe
- [ ] Ejemplos funcionales de uso
- [ ] Documentación técnica completa

---

## 🚀 Próximas Acciones

1. **Revisión del Client Brief**: Validar con stakeholders
2. **Setup del Ambiente**: Instalar Python 3.10+, crear venv
3. **Estructura Base**: Crear directorios y archivos base
4. **Primera Integración**: Audio input + STT básico
5. **Testing Continuo**: Validar cada componente conforme se implementa

---

## 📞 Contacto y Revisión

**Fecha de Última Revisión**: Mayo 2026  
**Próxima Revisión**: Tras completar Fase 2

---

*Este Client Brief sirve como guía general del proyecto y puede ser actualizado conforme se avanza en el desarrollo.*
