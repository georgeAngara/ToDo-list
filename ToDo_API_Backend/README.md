
# Prueba Técnica

Proyecto en FastAPI usando python 3.10, desplegado en Cloud Run GCP


# Descripción
Este sistema, describe el uso y puesta a punto de una **Api rest** usando [**Python**](https://www.python.org/downloads/) y [**FastAPI**](https://fastapi.tiangolo.com/)

![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)


## Objetivo
El objetivo es crear un **Api** de servicios para gestionar una lista de "tareas" (to-do).(crear, leer,actualizar y eliminar)



## Requisitos

- [**Python**](https://www.python.org/downloads/) 3.10.x
- [**virtualenv**](https://virtualenv.pypa.io/en/stable/) (Recomendado)
- [**Docker Desktop**](https://hub.docker.com/) (Si se quiere probar local)

## Recomendaciones
Para tener la facilidad de manejar multiples versiones de python, instalar y configurar el paquete [**pyenv**](https://github.com/pyenv/pyenv), para windows sería [**pyenv-win**](https://github.com/pyenv-win/pyenv-win)

### Explicación  instalación
**Harvey in Coding:** [_Canal youtube_](https://www.youtube.com/watch?v=aF0Ml39oRrE&t=740s)


## Instalación de este repositorio
Clonar este repositorio y alojarlo en una carpeta conveniente.

    git clone git@gitlab.com:jorgeluis163/my-movie-api-fastapi.git

Se recomienda usar [**virtualenv**](https://virtualenv.pypa.io/en/stable/) para desarrollo y pruebas.


## Activar virtualenv en entornos Windows

```sh
python -m virtualenv env
vanv\Scripts\activate

```

Otra forma:

```sh
python -m venv env
env\Scripts\activate

```
## Desactivar virtualenv en entornos Windows

```sh
deactivate
```


## Instalar las dependencias
Una vez dentro del entorno, instalar las dependencias:

```sh
(env) $ pip install -r requirements.txt
```
Otra forma:

```sh
python -m pip install -r requirements.txt
```

# Ejecutar local
para ejecutar local el proyeto:

```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

# Despliegue en Cloud Run
1. Inicializa GCP y activa Cloud Run:
```sh
gcloud init
gcloud config set project [TU_PROJECT_ID]
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
```

2. Build y deploy (Para windows):
```sh
gcloud run deploy api-backend --image gcr.io/[TU_PROJECT_ID]/api-backend --platform managed --region us-central1 --allow-unauthenticated
```
# Servicios y documentación

1. Url temporal del proyecto
```sh
https://api-backend-343319688013.us-central1.run.app
```
2. documentación de los servicios


**Servicios:** [_Documentación_](https://api-backend-343319688013.us-central1.run.app/docs)

