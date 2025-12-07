# Validador de Archivos - Django

Sistema de validación de archivos desarrollado con Django que permite verificar archivos planos de manera eficiente.

## Características

- Validación de tipos de archivo permitidos
- Verificación de tamaño de archivos
- Validación de formatos y estructuras
- Interfaz web intuitiva para carga de archivos
- Manejo de errores personalizado
- Feedback en tiempo real sobre el estado de validación

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (recomendado)

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/Deibyth/DesarrolloDJango_Validador.git
cd DesarrolloDJango_Validador
```

### Crear y activar entorno virtual

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install django

```

### Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

El proyecto estará disponible en: `http://127.0.0.1:8000/`


### Validación Básica de Archivos

1. Accede a la interfaz web
2. Selecciona el archivo que deseas validar
3. Haz clic en "Validar"
4. El sistema verificará:
   - Tipo de archivo permitido
   - Tamaño del archivo
   - Formato y estructura
5. Recibirás feedback inmediato sobre el resultado

### Validación en el Código

Ejemplo de validación personalizada en `forms.py`:

```python
from django import forms
from django.core.exceptions import ValidationError

class ArchivoForm(forms.Form):
    archivo = forms.FileField()
    
    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        
        # Validar extensión
        extensiones_permitidas = ['pdf', 'txt', 'csv', 'xlsx']
        ext = archivo.name.split('.')[-1].lower()
        
        if ext not in extensiones_permitidas:
            raise ValidationError(
                f'Extensión no permitida. Use: {", ".join(extensiones_permitidas)}'
            )
        
        # Validar tamaño (max 5MB)
        if archivo.size > 5 * 1024 * 1024:
            raise ValidationError('El archivo no puede superar 5MB')
        
        return archivo
```


### Configuraciones en `settings.py`

```python
# Tamaño máximo de archivo (en bytes)
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB

# Tipos MIME permitidos
ALLOWED_MIME_TYPES = [
    'application/pdf',
    'text/plain',
    'text/csv',
    'application/vnd.ms-excel',
]

# Extensiones permitidas
ALLOWED_EXTENSIONS = ['pdf', 'txt', 'csv', 'xlsx']
```







## Autor

**Deibith**
- GitHub: [@Deibyth](https://github.com/Deibyth)
