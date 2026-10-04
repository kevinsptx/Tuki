# 🎬 Tuki

Una app personal para llevar el registro de las películas que veo.
Guardo lo que vi, lo que quiero ver y qué tal me pareció.

> 🚧 En construcción. Es un proyecto para practicar Django por mi cuenta.

## Lo que quiero que tenga

- [ ] Registrar películas (título, año, puntuación, reseña)
- [ ] Géneros: varios por película
- [ ] Estados: pendiente y vista
- [ ] Editar y eliminar películas
- [ ] Búsqueda y filtros
- [ ] Inicio de sesión
- [ ] Diseño adaptado a celular y computador

## Hecho con

Python, Django, SQLite, HTML y CSS.

## Cómo correrlo

    git clone https://github.com/TU-USUARIO/tuki.git
    cd tuki
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Luego abre http://127.0.0.1:8000