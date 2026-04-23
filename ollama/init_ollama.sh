#!/bin/bash

# Script para inicializar Ollama con los modelos necesarios para el proyecto EPUB

echo "🚀 Inicializando Ollama para el proyecto EPUB Structure Extractor..."

# Esperar a que Ollama esté disponible
echo "⏳ Esperando que Ollama esté disponible..."
while ! curl -s http://localhost:11434/api/tags > /dev/null; do
    echo "   Ollama no está disponible aún, esperando 5 segundos..."
    sleep 5
done

echo "✅ Ollama está disponible!"

# Descargar modelo principal para análisis de texto
echo "📥 Descargando modelo principal llama3.1:8b..."
curl -X POST http://localhost:11434/api/pull \
    -H "Content-Type: application/json" \
    -d '{"name": "llama3.1:8b"}' &

# Descargar modelo de embeddings
echo "📥 Descargando modelo de embeddings nomic-embed-text..."
curl -X POST http://localhost:11434/api/pull \
    -H "Content-Type: application/json" \
    -d '{"name": "nomic-embed-text"}' &

# Opcional: Descargar modelo más pequeño para pruebas rápidas
echo "📥 Descargando modelo ligero llama3.2:1b para pruebas..."
curl -X POST http://localhost:11434/api/pull \
    -H "Content-Type: application/json" \
    -d '{"name": "llama3.2:1b"}' &

# Esperar a que terminen las descargas
wait

echo "🎉 ¡Inicialización completada!"
echo ""
echo "Modelos disponibles:"
curl -s http://localhost:11434/api/tags | jq '.models[].name' || echo "   (jq no disponible para formatear JSON)"

echo ""
echo "🔧 Servicios disponibles:"
echo "   - Ollama: http://localhost:11434"
echo "   - ChromaDB: http://localhost:8000"
echo "   - Qdrant: http://localhost:6333"
echo ""
echo "Para usar los modelos en tu código Python:"
echo "   import ollama"
echo "   response = ollama.chat(model='llama3.1:8b', messages=[{'role': 'user', 'content': 'Hola'}])"