# EPUB to PDF Structure Generator

Un script en Python para extraer el índice y la estructura de capítulos y subcapítulos de archivos EPUB y generar un documento PDF con la estructura jerárquica.

## Características

- ✅ Extrae la tabla de contenidos (TOC) de archivos EPUB
- ✅ Genera PDF con estructura jerárquica de capítulos y subcapítulos
- ✅ Soporte para archivos NCX (Navigation Control file for XML)
- ✅ Método de respaldo usando la estructura del spine
- ✅ Estilos profesionales con diferentes niveles de indentación
- ✅ Contenedor Docker para fácil despliegue
- ✅ Variables de entorno para configuración flexible
- ✅ Docker Compose para ejecución simplificada

## Uso

### Uso directo con Python

```bash
# Uso básico
python epub_to_pdf.py archivo.epub

# Especificar archivo de salida
python epub_to_pdf.py libro.epub --output mi_estructura.pdf
```

### Uso con Docker

#### Opción 1: Docker Run
```bash
# Crear directorio de salida
mkdir -p output

# Ejecutar contenedor
docker build -t epub-to-pdf .
docker run -e EPUB_FILE=my_epub.epub \
  -v $(pwd):/app/input:ro \
  -v $(pwd)/output:/app/output \
  epub-to-pdf
```

#### Opción 2: Docker Compose (Recomendado)
```bash
# Configurar variables de entorno
cp .env.example .env
# Editar .env con tu archivo EPUB

# Ejecutar
docker-compose up
```

### Variables de entorno

- `EPUB_FILE`: Nombre del archivo EPUB a procesar (requerido)
- `OUTPUT_FILE`: Nombre del archivo PDF de salida (opcional)
- `INPUT_PATH`: Directorio donde están los archivos EPUB (default: ./)
- `OUTPUT_PATH`: Directorio donde guardar los PDFs (default: ./output)

## Ejemplo de salida

El script genera un PDF profesional con:

### Contenido del PDF
- **Título del libro** centrado y estilizado
- **Índice de contenidos** con jerarquía visual
- **Capítulos y subcapítulos** con diferentes niveles de indentación
- **Resumen** con total de capítulos encontrados
- **Información del archivo** fuente

### Ejemplo de estructura generada:
```
Estructura del Libro
Official Google Cloud Certified Professional Machine Learning Engineer Study Guide

Índice de Contenidos

Introduction
Part I: Foundational Knowledge
    Chapter 1: Introduction to Machine Learning on Google Cloud
    Chapter 2: Google Cloud ML Services Overview
Part II: Advanced Topics
    Chapter 3: ML Pipelines and Automation
    Chapter 4: Model Deployment and Monitoring

Total de capítulos encontrados: 4
Archivo EPUB: my_epub.epub
```

## Cómo funciona

El script funciona siguiendo estos pasos:

1. **Abre el archivo EPUB** como un archivo ZIP (los EPUB son archivos ZIP con una estructura específica)
2. **Lee el container.xml** para encontrar la ubicación del archivo OPF (Open Packaging Format)
3. **Analiza el archivo OPF** para localizar el archivo NCX (Navigation Control file)
4. **Extrae la estructura** del archivo NCX que contiene la tabla de contenidos
5. **Como respaldo**, si no encuentra NCX, usa la estructura del spine para extraer los capítulos

## Estructura de archivos EPUB

Los archivos EPUB tienen la siguiente estructura típica:
```
libro.epub
├── META-INF/
│   └── container.xml
├── OEBPS/
│   ├── content.opf (archivo OPF)
│   ├── toc.ncx (archivo NCX con tabla de contenidos)
│   ├── Text/
│   │   ├── chapter1.xhtml
│   │   ├── chapter2.xhtml
│   │   └── ...
│   └── ...
└── mimetype
```

## Requisitos

### Para uso directo
- Python 3.6 o superior
- ReportLab para generación de PDFs

### Para uso con Docker
- Docker
- Docker Compose (opcional, pero recomendado)

## Instalación

### Instalación directa

1. Clona este repositorio:
```bash
git clone https://github.com/josueelias9/extract-structure-from-epub-file.git
cd extract-structure-from-epub-file
```

2. Instala dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el script:
```bash
python epub_to_pdf.py tu_archivo.epub
```

### Instalación con Docker

1. Clona el repositorio:
```bash
git clone https://github.com/josueelias9/extract-structure-from-epub-file.git
cd extract-structure-from-epub-file
```

2. Configura las variables de entorno:
```bash
cp .env.example .env
# Edita .env con el nombre de tu archivo EPUB
```

3. Ejecuta con Docker Compose:
```bash
docker-compose up
```

## Limitaciones

- El script está optimizado para archivos EPUB estándar que siguen las especificaciones EPUB 2.0 y 3.0
- Algunos archivos EPUB muy antiguos o mal formateados pueden no ser procesados correctamente
- La extracción de títulos desde HTML es básica y puede no capturar títulos complejos con formato especial

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.