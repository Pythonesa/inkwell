# Configuración del entorno de desarrollo

## Requisitos previos

- Python (para poder utilizar pip).
- Virtualenv (si no lo tienes `pip install virtualenv`).

## Entorno virtual

### Crear un entorno virtual

```bash
python -m venv .venv
```

### Activar el entorno virtual

En Linux/MacOS:

```bash
source .venv/bin/activate
```

En Windows:

```bash
.\.venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Aplicar migraciones iniciales

```bash
python manage.py migrate
```

## Crear un super usuario

```bash
python manage.py createsuperuser
```

## Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Accede a <http://127.0.0.1:8000/admin> y verifica que puedes iniciar sesión con el super usuario creado.
