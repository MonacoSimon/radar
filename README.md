# Radar — Portal de Noticias

Portal de noticias desarrollado con **Django**, como proyecto académico de la carrera de Software Libre de la Universidad Nacional del Litoral (UNL).

Radar permite publicar y consultar artículos organizados por categorías, visualizar perfiles de autores, realizar comentarios y enviar mensajes mediante un formulario de contacto.

---

## Tabla de contenidos

- [Descripción del proyecto](#descripción-del-proyecto)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Requisitos previos](#requisitos-previos)
- [Instalación y configuración](#instalación-y-configuración)
- [Ejecución del proyecto](#ejecución-del-proyecto)
- [Aplicaciones de Django](#aplicaciones-de-django)
- [Modelos y relaciones](#modelos-y-relaciones)
- [Funcionalidades](#funcionalidades)
- [Panel de administración](#panel-de-administración)
- [Archivos estáticos e imágenes](#archivos-estáticos-e-imágenes)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Consultas ORM](#consultas-orm)
- [Rutas principales](#rutas-principales)
- [Autoría](#autoría)

---

## Descripción del proyecto

**Radar** es un portal web de noticias que permite gestionar y consultar información organizada en diferentes categorías.

El proyecto fue desarrollado utilizando Django y sigue una estructura modular, separando las responsabilidades en distintas aplicaciones.

Los visitantes pueden consultar artículos publicados, explorar categorías, conocer a los autores, dejar comentarios y comunicarse mediante un formulario de contacto.

Además, cuenta con un panel de administración que permite gestionar el contenido y moderar los comentarios recibidos.

## Tecnologías utilizadas

| Tecnología | Utilización |
|---|---|
| Python 3.12.3 | Lenguaje de programación |
| Django | Framework de desarrollo web |
| SQLite | Base de datos |
| Pillow | Gestión y procesamiento de imágenes |
| HTML5 | Estructura de las páginas |
| CSS3 | Diseño y presentación visual |
| Django Templates | Renderizado dinámico de páginas |
| Django ORM | Consultas y gestión de datos |

Las dependencias del proyecto se encuentran registradas en `requirements.txt`.

## Requisitos previos

Para instalar y ejecutar el proyecto se necesita:

- Python 3.12.3 o compatible.
- pip.
- Entorno virtual de Python.
- Git (opcional, para clonar el repositorio).

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/MonacoSimon/radar.git
```

Ingresar al directorio del proyecto:

```bash
cd radar
```

> Reemplazar `URL_DEL_REPOSITORIO` por la dirección correspondiente al repositorio.

### 2. Crear el entorno virtual

```bash
python3 -m venv venv
```

### 3. Activar el entorno virtual

En Linux o Ubuntu:

```bash
source venv/bin/activate
```

### 4. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Aplicar las migraciones

```bash
python manage.py migrate
```

Este comando crea las tablas necesarias en la base de datos SQLite.

### 6. Crear un superusuario

```bash
python manage.py createsuperuser
```

Se solicitarán los datos necesarios para crear una cuenta con acceso al panel de administración.

### 7. Comprobar la configuración

```bash
python manage.py check
```

Este comando permite detectar problemas en la configuración del proyecto.

## Ejecución del proyecto

Con el entorno virtual activado, ejecutar:

```bash
python manage.py runserver
```

El servidor de desarrollo estará disponible en:

**http://127.0.0.1:8000/**

Para acceder al panel de administración:

**http://127.0.0.1:8000/admin/**

---

## Aplicaciones de Django

El proyecto está organizado en seis aplicaciones propias, además de las seis aplicaciones predeterminadas de Django.

| Aplicación | Responsabilidad |
|---|---|
| `paginas` | Página de inicio y sección Acerca de. |
| `articulos` | Gestión, listado y detalle de artículos. |
| `autores` | Perfiles y datos de los autores. |
| `categorias` | Organización de artículos por categorías. |
| `comentarios` | Gestión y moderación de comentarios. |
| `contacto` | Formulario de contacto y almacenamiento de mensajes. |

Esta separación permite mantener el código organizado y facilita el mantenimiento y la ampliación del proyecto.

## Modelos y relaciones

El proyecto cuenta con cinco modelos principales:

### Categoria

Representa las categorías utilizadas para organizar los artículos.

Campos principales:

- `nombre`
- `slug`
- `descripcion`

### Autor

Almacena la información de los autores.

Campos principales:

- `nombre`
- `apellido`
- `email`
- `biografia`
- `foto_perfil`
- `activo`
- `fecha_registro`

### Articulo

Representa el contenido principal del portal.

Campos principales:

- `titulo`
- `subtitulo`
- `slug`
- `contenido`
- `imagen`
- `estado`
- `fecha_creacion`
- `fecha_publicacion`
- `contador_visitas`
- `autor`
- `categoria`

El campo `estado` utiliza las siguientes opciones:

- Borrador.
- Publicado.
- Archivado.

Los artículos se relacionan con un autor y una categoría mediante claves foráneas (`ForeignKey`).

### Comentario

Almacena los comentarios realizados por los visitantes.

Campos principales:

- `contenido`
- `nombre`
- `email`
- `estado`
- `fecha_creacion`
- `votos_favoritos`
- `articulo`

Los comentarios tienen tres estados posibles:

- Pendiente.
- Aprobado.
- Rechazado.

Cada comentario pertenece a un artículo.

### MensajeContacto

Almacena los mensajes enviados mediante el formulario de contacto.

Campos principales:

- `nombre`
- `email`
- `asunto`
- `mensaje`
- `fecha_envio`
- `leido`

Los campos `fecha_envio` y `leido` permiten registrar cuándo se recibió el mensaje y si ya fue revisado.

### Relaciones entre modelos

Las relaciones principales son:

- **Autor – Artículo:** relación uno a muchos. Un autor puede escribir varios artículos, pero cada artículo pertenece a un autor.
- **Categoría – Artículo:** relación uno a muchos. Una categoría puede contener varios artículos, pero cada artículo pertenece a una categoría.
- **Artículo – Comentario:** relación uno a muchos. Un artículo puede tener varios comentarios, pero cada comentario pertenece a un artículo.

---

## Funcionalidades

### Página de inicio

- Muestra los cinco artículos publicados más recientes.
- Presenta imágenes, títulos y datos de los artículos.
- Permite acceder al detalle de cada publicación.
- Muestra las categorías disponibles.

### Artículos

- Listado de artículos publicados.
- Vista individual con el contenido completo.
- Visualización de imágenes, autor y categoría.
- Paginación de seis artículos por página.
- Navegación entre páginas.

### Categorías

- Listado de categorías disponibles.
- Descripción de cada categoría.
- Visualización de los artículos asociados.
- Acceso al detalle de cada artículo.

### Autores

- Listado de autores activos.
- Visualización de fotografías de perfil.
- Perfil individual con biografía y datos del autor.
- Listado de sus artículos publicados.

### Comentarios

- Formulario para dejar comentarios en los artículos.
- Validación de los datos enviados.
- Los comentarios se guardan inicialmente con estado pendiente.
- Moderación desde el panel de administración.
- Visualización pública únicamente de comentarios aprobados.

### Contacto

- Formulario con los campos nombre, email, asunto y mensaje.
- Validación de los datos ingresados.
- Almacenamiento de los mensajes en la base de datos.
- Página de confirmación después del envío.
- Gestión de mensajes desde el panel de administración.

### Acerca de

Página informativa que presenta el propósito del portal.

---

## Panel de administración

Radar utiliza el panel de administración integrado de Django.

Desde allí se pueden gestionar los siguientes modelos:

- Categorías.
- Autores.
- Artículos.
- Comentarios.
- Mensajes de contacto.

Se personalizó la administración de los modelos mediante diferentes opciones de Django Admin:

| Opción | Función |
|---|---|
| `list_display` | Define las columnas visibles en los listados. |
| `list_filter` | Agrega filtros laterales. |
| `search_fields` | Permite buscar registros. |
| `prepopulated_fields` | Genera automáticamente el slug a partir de otros campos. |
| `date_hierarchy` | Facilita la navegación por fechas. |

La administración de artículos cuenta con una configuración específica para facilitar la gestión del contenido.

---

## Archivos estáticos e imágenes

El proyecto separa los archivos estáticos de los archivos multimedia.

### Archivos estáticos

Se encuentran en la carpeta `static/`.

Incluyen:

- `css/`: hojas de estilo.
- `js/`: archivos JavaScript.
- `img/`: imágenes utilizadas por el diseño del sitio.

La hoja de estilos principal es:

```text
static/css/style.css
```

La configuración se encuentra en `radar/settings.py`:

```python
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

### Archivos multimedia

Las imágenes cargadas desde el panel de administración se almacenan en `media/`.

Se organizan en:

- `media/autores/`: fotografías de perfil.
- `media/articulos/`: imágenes de artículos.

Configuración:

```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Para el entorno de desarrollo, las rutas multimedia se habilitan desde `radar/urls.py`.

---

## Estructura del proyecto

La organización general del proyecto es la siguiente:

```text
radar/
│
├── articulos/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── autores/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── categorias/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── comentarios/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── contacto/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── paginas/
│   ├── migrations/
│   ├── apps.py
│   ├── urls.py
│   └── views.py
│
├── radar/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   ├── articulos/
│   ├── autores/
│   ├── categorias/
│   ├── comentarios/
│   ├── contacto/
│   ├── paginas/
│   └── base.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   └── img/
│
├── media/
│   ├── autores/
│   └── articulos/
│
├── venv/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

> La estructura muestra la organización general del proyecto. Las carpetas de migraciones contienen los archivos generados por Django.

---

## Consultas ORM

Django ORM permite consultar y manipular los datos sin necesidad de escribir SQL directamente.

Para ingresar a la consola interactiva:

```bash
python manage.py shell
```

Importar los modelos:

```python
from articulos.models import Articulo
from autores.models import Autor
from categorias.models import Categoria
from comentarios.models import Comentario
```

### Ejemplos de consultas

Obtener todos los artículos:

```python
Articulo.objects.all()
```

Obtener los cinco artículos más recientes:

```python
Articulo.objects.order_by('-fecha_creacion')[:5]
```

Buscar artículos de una categoría:

```python
Articulo.objects.filter(categoria__nombre='Tecnología')
```

Buscar artículos de un autor:

```python
Articulo.objects.filter(autor__nombre='Martín')
```

Obtener artículos publicados:

```python
Articulo.objects.filter(estado='publicado')
```

Consultar comentarios de artículos de una categoría:

```python
Comentario.objects.filter(articulo__categoria__nombre='Deportes')
```

---

## Rutas principales

| Dirección | Descripción |
|---|---|
| `/` | Página de inicio. |
| `/acerca/` | Información sobre el portal. |
| `/articulos/` | Listado de artículos. |
| `/articulos/<slug>/` | Detalle de un artículo. |
| `/categorias/` | Listado de categorías. |
| `/categorias/<slug>/` | Detalle de una categoría. |
| `/autores/` | Listado de autores. |
| `/autores/<id>/` | Perfil individual de un autor. |
| `/comentarios/nuevo/<id>/` | Formulario para comentar un artículo. |
| `/contacto/` | Formulario de contacto. |
| `/contacto/exito/` | Confirmación del envío del mensaje. |
| `/admin/` | Panel de administración de Django. |

---

## Autoría

**Proyecto:** Radar — Portal de Noticias.

**Institución:** Universidad Nacional del Litoral (UNL).

**Carrera:** Software Libre.

**Tecnologías principales:** Python y Django.

Proyecto desarrollado con fines académicos.