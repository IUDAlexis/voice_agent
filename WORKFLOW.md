# Claude Code Workflow - Voice Agent

## 📋 Flujo de Desarrollo con Claude Code

Este documento describe cómo se aplica el **flujo de desarrollo moderno con Claude Code** en el proyecto Voice Agent, siguiendo las mejores prácticas para desarrollo ágil y colaborativo.

---

## 🔄 Fases del Workflow

### Fase 1️⃣: **Investigación y Planificación**

**Objetivo**: Entender profundamente los requisitos antes de escribir código.

#### Proceso
1. **Análisis de Requisitos**
   - Leer el Client Brief completamente
   - Identificar componentes principales
   - Definir interfaces y contratos entre módulos

2. **Investigación Técnica**
   ```
   Preguntas a responder:
   ✓ ¿Qué frameworks existen? (Pipecat, LiveKit Agents)
   ✓ ¿Cuál es la arquitectura estándar?
   ✓ ¿Qué librerías usar? (asyncio, PyAudio, etc.)
   ✓ ¿Cuáles son los trade-offs?
   ```

3. **Planificación de Arquitectura**
   - Diagrama de componentes
   - Flujo de datos
   - Dependencias entre módulos
   - Points de integración

4. **Definición de Interfaces**
   - Clases base abstractas
   - Métodos y signatures
   - Tipos de entrada/salida
   - Manejo de errores esperados

**Salida**: CLIENT_BRIEF.md, README.md, diagramas

---

### Fase 2️⃣: **Implementación Iterativa con Claude Code**

**Objetivo**: Escribir código de calidad de forma incremental.

#### Proceso

**A. Generar Estructura Base**
```
Claude Code → Estructura de directorios
              → __init__.py para cada módulo
              → Archivos base vacíos
              → Importaciones necesarias
```

**B. Implementar una Clase Base Abstracta**
```
Ejemplo: STTProvider

Claude Code:
1. Leer Client Brief para entender requisitos de STT
2. Analizar interfaces de frameworks similares
3. Generar clase abstracta con:
   - Métodos abstractos
   - Docstrings completos
   - Type hints
   - Logging

Revisar:
✓ ¿Los métodos tienen sentido?
✓ ¿Los parámetros son correctos?
✓ ¿El error handling está claro?
✓ ¿Hay ejemplos de uso?
```

**C. Implementar Providers Concretos**
```
Ejemplo: WhisperSTT

Claude Code:
1. Heredar de STTProvider
2. Implementar método abstracto transcribe()
3. Usar OpenAI API
4. Agregar error handling específico
5. Agregar logging

Revisar:
✓ ¿La implementación sigue el contrato?
✓ ¿Se manejan errores de API?
✓ ¿El async/await está correcto?
✓ ¿Hay memory leaks potenciales?
```

**D. Crear Mock Provider para Testing**
```
Ejemplo: MockSTT

Claude Code:
1. Implementar mismo interfaz que WhisperSTT
2. Retornar datos ficticios
3. Simular comportamientos

Valor:
✓ Permite testing sin APIs
✓ No consume cuota de APIs
✓ Testing determinístico
```

#### Ciclo Iterativo Básico
```
┌─────────────────────────────────────┐
│ 1. Generar estructura con Claude    │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ 2. Revisar y entender el código     │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ 3. Hacer ajustes/refinamientos      │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ 4. Guardar y versionar (git)        │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│ 5. Siguiente componente             │
└─────────────────────────────────────┘
```

**Key Decisions Made with Claude Code**:

1. **Arquitectura Modular**
   - Cada componente (STT, LLM, TTS) tiene su propio módulo
   - Base abstracta + implementaciones concretas
   - Fácil para cambiar providers

2. **Asyncio First**
   - Todo es async desde el inicio
   - No hay I/O bloqueante
   - Thread pool para operaciones I/O pesadas

3. **Type Hints Completos**
   - Validación estática
   - Mejor IDE support
   - Documentación implícita

4. **Mock Providers**
   - Testing sin APIs externas
   - Desarrollo sin API keys
   - Determinístico

---

### Fase 3️⃣: **Validación y Testing**

**Objetivo**: Asegurar calidad del código.

#### Proceso

**A. Type Checking**
```bash
mypy src/
```
- Valida tipos
- Encuentra errores antes de runtime
- Integrado en workflow CI/CD

**B. Linting**
```bash
flake8 src/
black src/
```
- Estilo de código consistente
- Evita bugs comunes
- Mejor legibilidad

**C. Unit Tests**
```python
# tests/test_stt.py

@pytest.mark.asyncio
async def test_whisper_initialization():
    stt = WhisperSTT()
    await stt.initialize()
    # assertions...

@pytest.mark.asyncio
async def test_transcribe_error_handling():
    stt = WhisperSTT()
    # Test error cases
```

**D. Integration Tests**
```python
# tests/test_agent.py

@pytest.mark.asyncio
async def test_full_pipeline():
    agent = VoiceAgent(use_mock=True)
    await agent.initialize()
    
    # Run a full cycle
    audio = await agent.listen_for_speech()
    response = await agent.process_pipeline(audio)
    
    assert response is not None
    await agent.cleanup()
```

#### Testing Strategy

| Tipo | Scope | Speed | Cost |
|------|-------|-------|------|
| Unit | Individual functions | Muy rápido | Bajo |
| Integration | Component interactions | Rápido | Medio |
| E2E | Full pipeline | Lento | Alto |

**Enfoque**: Muchos unit tests + algunos integration tests + pocos E2E

---

### Fase 4️⃣: **Documentación y Entrega**

**Objetivo**: Hacer el código accesible a otros desarrolladores.

#### Proceso

**A. Docstrings en Código**
```python
def synthesize(self, text: str) -> np.ndarray:
    """Synthesize text to audio
    
    This method converts text to speech audio using the TTS engine.
    The audio is returned as a NumPy array for easy integration.
    
    Args:
        text: Text to synthesize (required)
        
    Returns:
        Audio samples as NumPy int16 array at 16kHz
        
    Raises:
        RuntimeError: If TTS engine not initialized
        ValueError: If text is empty
        
    Example:
        >>> tts = Pyttsx3TTS()
        >>> await tts.initialize()
        >>> audio = await tts.synthesize("Hola")
        >>> audio.shape
        (16000,)
    """
```

**B. Documentación Externa**
- README.md: Overview del proyecto
- docs/architecture.md: Diagramas y flujos
- docs/setup.md: Instalación paso a paso
- docs/api.md: Referencia de API
- CLIENT_BRIEF.md: Contexto y requisitos

**C. Ejemplos de Código**
```python
# examples/basic_agent.py

async def main():
    """Simple example of using Voice Agent"""
    agent = VoiceAgent(use_mock=True)
    await agent.initialize()
    
    # One full interaction
    audio = await agent.listen_for_speech()
    response = await agent.process_pipeline(audio)
    
    await agent.cleanup()
```

**D. README en Cada Directorio**
```
src/
├── stt/
│   ├── README.md  ← Documentación del módulo
│   ├── base.py
│   └── providers.py
```

---

## 🛠️ Tools y Técnicas con Claude Code

### 1. **Code Generation**

Claude Code es especialmente útil para:

✅ **Generar estructura boilerplate**
```
"Create a base class for STT providers with these methods: transcribe, initialize, cleanup"
```

✅ **Generar múltiples implementaciones**
```
"Create WhisperSTT, GoogleSTT, and AzureSTT implementations"
```

✅ **Generar tests**
```
"Generate unit tests for the Microphone class"
```

✅ **Generar documentación**
```
"Create API documentation for all STT providers"
```

### 2. **Code Analysis**

Claude Code es útil para:

✅ **Revisar arquitectura**
```
"Is this async architecture correct? Any bottlenecks?"
```

✅ **Identificar patrones**
```
"Which design patterns are used here? Any anti-patterns?"
```

✅ **Performance analysis**
```
"What's the latency bottleneck in this pipeline?"
```

### 3. **Code Refactoring**

Claude Code puede:

✅ **Mejorar legibilidad**
```
"Refactor this code to be more readable"
```

✅ **Reducir duplicación**
```
"DRY up this code - there's repeated patterns"
```

✅ **Optimizar performance**
```
"Optimize this for lower latency"
```

---

## 📊 Workflow Actual de Este Proyecto

### Paso 1: Estructura Base ✅
```
Claude Code → Generar estructura de directorios
            → Crear __init__.py para cada módulo
            → Crear archivos base
```

### Paso 2: Clases Base ✅
```
Claude Code → Generar STTProvider abstracta
            → Generar LLMProvider abstracta
            → Generar TTSProvider abstracta
```

### Paso 3: Implementations ✅
```
Claude Code → Generar WhisperSTT
            → Generar MockSTT
            → Generar OpenAILLM
            → Generar MockLLM
            → Generar Pyttsx3TTS
            → Generar MockTTS
```

### Paso 4: Audio I/O ✅
```
Claude Code → Generar Microphone class
            → Generar Speaker class
            → Agregar async I/O
```

### Paso 5: Agent Core ✅
```
Claude Code → Generar VoiceAgent orchestrator
            → Generar AgentStateMachine
            → Generar main event loop
```

### Paso 6: Configuration ✅
```
Claude Code → Generar config.py
            → Generar .env.example
            → Agregar validación
```

### Paso 7: Documentation ✅
```
Claude Code → Generar README.md
            → Generar CLIENT_BRIEF.md
            → Generar docs/*.md
            → Generar docstrings
```

### Paso 8: Testing (Próximo)
```
Claude Code → Generar test suite
            → Generar fixtures
            → Generar mocks
```

---

## 📈 Beneficios del Workflow con Claude Code

### Para el Desarrollo
- ⚡ **Velocidad**: Generar código base rápidamente
- 🎯 **Enfoque**: Claude maneja boilerplate, tú enfocado en lógica
- 🔄 **Iteración**: Fácil refactor y mejora
- 📚 **Documentación**: Automática con docstrings

### Para el Equipo
- 🤝 **Consistencia**: Mismo style y patterns
- 📖 **Onboarding**: Código bien documentado
- 🔍 **Mantenibilidad**: Código limpio y estructurado
- ✅ **Calidad**: Type hints y tests desde inicio

### Para el Proyecto
- 🚀 **Go-to-market**: MVP rápido
- 📦 **Modularidad**: Fácil de extender
- 🔌 **Flexibility**: Providers intercambiables
- 📊 **Escalabilidad**: Arquitectura preparada

---

## 🎓 Lecciones Aprendidas

### ✅ Qué Funcionó Bien
1. **Empezar con estructura clara** antes de código
2. **Type hints desde el inicio** - ahorra debugging
3. **Mock providers** - permite testing sin APIs
4. **Abstract base classes** - facilita extensión
5. **Asyncio desde el inicio** - no hay refactoring después

### ⚠️ Qué Evitar
1. Cambiar arquitectura después de empezar
2. Olvidar documentación hasta el final
3. No usar type hints
4. Hardcodear valores
5. Ignorar error handling

### 💡 Recomendaciones
1. **Separar concerns**: Cada módulo una responsabilidad
2. **Usar interfaces**: Contrato claro entre componentes
3. **Testeable desde inicio**: Mock providers ayudan
4. **Documentar decisiones**: Por qué, no solo qué

---

## 🔄 Próximas Iteraciones

### Próximo Sprint
- [ ] Implementar tests completos
- [ ] Integración real con APIs
- [ ] Performance tuning
- [ ] Error recovery robusta

### Mejoras Futuras
- [ ] Multi-language support
- [ ] Voice activity detection
- [ ] Context management mejorado
- [ ] Plugin system para providers
- [ ] WebSocket para remote clients

---

## 📝 Resumen: Flujo de Desarrollo

```
1. ENTENDER
   └─ Leer requisitos
   └─ Investigar tecnologías
   └─ Definir arquitectura

2. PLANIFICAR
   └─ Definir interfaces
   └─ Crear diagramas
   └─ Identificar componentes

3. GENERAR (Claude Code)
   └─ Boilerplate y estructura
   └─ Clases base
   └─ Implementaciones
   └─ Tests y docs

4. REVISAR
   └─ Type checking
   └─ Linting
   └─ Architecture review
   └─ Performance check

5. VALIDAR
   └─ Unit tests
   └─ Integration tests
   └─ Manual testing

6. DOCUMENTAR
   └─ Docstrings
   └─ README
   └─ Ejemplos
   └─ API docs

7. ENTREGAR
   └─ Git commit
   └─ GitHub issues
   └─ Release notes
```

---

**Última actualización**: Mayo 2026  
**Documento**: Guía de Workflow con Claude Code  
**Proyecto**: Voice Agent - Agente de Voz Conversacional
