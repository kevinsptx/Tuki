# 🎬 Tuki

Tuki es una aplicación personal sencilla para llevar un registro de las películas que veo y de las que quiero ver.

La aplicación permite guardar las películas que ya vi, ponerles una calificación y escribir un comentario sobre ellas. También puedo guardar películas pendientes para tener una lista de las que quiero ver después.

## ✨ Funciones

* 🎬 Registrar películas vistas.
* ⭐ Calificar las películas del 1 al 10.
* 💬 Agregar un comentario sobre cada película.
* 📅 Guardar automáticamente la fecha en que se registra una película.
* 🎞️ Registrar películas pendientes.
* ✏️ Editar películas vistas y pendientes.
* 🗑️ Eliminar películas vistas y pendientes.
* 🔐 Inicio de sesión para acceder a la aplicación.
* 📱 Diseño adaptado para computador y celular.

## 🛠️ Tecnologías

* Python
* Django
* SQLite
* HTML
* CSS

## 📂 Estructura principal

Tuki está desarrollado con Django y cuenta con las siguientes funcionalidades principales:

* **Películas vistas:** muestra las películas que ya he visto, su calificación, comentario y fecha.
* **Películas pendientes:** muestra las películas que quiero ver después.
* **Registro:** permite agregar nuevas películas vistas o pendientes.
* **Edición:** permite actualizar la información registrada.
* **Eliminación:** permite eliminar películas de las listas.

## 🚀 Cómo ejecutar el proyecto

Clona el repositorio:

```
git clone https://github.com/TU-USUARIO/tuki.git
```

Entra a la carpeta:

```
cd tuki
```

Crea el entorno virtual:

```
python -m venv .venv
```

Activa el entorno virtual en Linux:

```
source .venv/bin/activate
```

Instala las dependencias:

```
pip install -r requirements.txt
```

Realiza las migraciones:

```
python manage.py migrate
```

Inicia el servidor:

```
python manage.py runserver
```

Luego abre en el navegador:

```
http://127.0.0.1:8000
```

## 🎯 Objetivo del proyecto

Tuki fue creado como un proyecto personal para practicar el desarrollo de aplicaciones web con Django.

La idea principal fue hacer una aplicación sencilla y funcional para organizar mis películas sin agregar funciones innecesarias.

## 👨‍💻 Autor

Kevin Santiago Patiño
