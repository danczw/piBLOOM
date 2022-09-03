# piBLOOM - Raspberry Pi based BLOOM model serving

**A web application and REST API for serving the BLOOM model via a Raspberry Pi cluster.**

The **BLOOM model**, developed by [BigScience](https://bigscience.huggingface.co) is a transformer based autoregressive Large Language Model (LLM). It is trained to continue text from a prompt on vast amounts of text data using industrial-scale computational resources. As such, it is able to output coherent text in 46 languages and 13 programming languages that is hardly distinguishable from text written by humans. The model is available for download from the [HuggingFace repository](https://huggingface.co/bigscience/bloom), including detailed [model documentation](https://huggingface.co/docs/transformers/model_doc/bloom).

Goal of the project is to serve a simple web app and REST API which allows to "chat" with the BLOOM model of a small [Raspberry Pi](https://www.raspberrypi.org) cluster of approximately 2-4 [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/).

<br>

----------------
----------------

<br>

## Quick Setup

Expose web application, including middleware, application server and model serving API to `http://localhost:80` by running:

```bash
    docker compose up -- build
```

Attention: See `README.txt` ([./pibloom_api/model/README.txt](./pibloom_api/model/README.txt)) and update `.env` ([./pibloom_web/.env.example](./pibloom_web/.env.example)) to before running any setups!

<br>

----------------
----------------

<br>

## Project Structure

<br>

    piBLOOM
    ├─ .gitignore
    ├─ docker-compose.yml           # Docker entry point for deployment
    ├─ LICENSE
    ├─ pibloom_api                  # API for serving BLOOM model prompts
    │  ├─ .dockerignore
    │  ├─ config.yml                # - Configuration for API logging
    │  ├─ Dockerfile
    │  ├─ model
    │  │  └─ README.txt             # - Docs on model download instructions
    │  ├─ pibloom
    │  │  ├─ app.py                 # - API entry point
    │  │  ├─ model.py               # - BLOOM model class
    │  │  └─ __init__.py
    │  ├─ poetry.lock               # - Poetry API dependencies
    │  ├─ pyproject.toml            # - Poetry project setup
    │  └─ tests                     # - API testing
    │     ├─ test_pibloom.py
    │     └─ __init__.py
    ├─ pibloom_proxy                # Web app reverse proxy
    │  ├─ default.conf              # - Nginx configuration
    │  └─ Dockerfile
    ├─ pibloom_web                  # Web application for API interaction
    │  ├─ .dockerignore
    │  ├─ .env.example              # - .env example file for env var definitions
    │  ├─ .gitignore
    │  ├─ Dockerfile
    │  ├─ index.html
    │  ├─ package-lock.json         # - Web application dependencies
    │  ├─ package.json
    │  ├─ public
    │  │  └─ [...]
    │  ├─ server
    │  │  └─ server.js              # - Entrypoint for expressjs middleware
    │  ├─ src
    │  │  ├─ App.vue
    │  │  ├─ assets
    │  │  │  └─ [...]
    │  │  ├─ components
    │  │  │  └─ HelloWorld.vue
    │  │  ├─ main.js
    │  │  ├─ router                 # - Web application site routing
    │  │  │  └─ index.js
    │  │  └─ views
    │  │     ├─ AboutView.vue       # - Vue view about project
    │  │     └─ HomeView.vue        # - Main Vue View for model API interaction
    │  └─ vite.config.js
    └─ README.md

The API, web application and proxy server can be served using [Docker](https://www.docker.com), utilizing the `docker-compose.yml` [file](./docker-compose.yml).

Simply install Docker and build the images via:

    `docker compose build`

You can increase the number of workers for the API by increasing the `N_WORKERS` argument in the [docker-compose.yml](./docker-compose.yml) file.

Then start the container using:

    `docker compose up`

[NGINX](https://www.nginx.com) is used as a reverse proxy and load balancer to manage incoming traffic and distribute it to the slower upstream web application server. NGINX allows to hide the web server IP address to the client, making the server more secure.

Alternatively, the API and web application can be served individually (e.g. for development purposes) as per the setup steps below.

<br>

----------------
----------------

<br>

## Development Setup

<br>

### 1. piBLOOM API server

<br>

The model is not loaded from the HuggingFace Hub, but from the local filesystem. Make sure to download 

- config.json
- pytorch_model.bin
- special_tokens_map.json
- tokenizer.json
- tokenizer.json

from [HuggingFace Repo](https://huggingface.co/bigscience/bloom-560m/tree/main) and save them to `./pibloom_api/model/`.

<br>

**Local setup without Docker**

The project uses [Poetry](https://python-poetry.org) to manage the project dependencies. Install dependencies within the respective subfolder via:

    `cd pibloom_api/`
    `poetry install`


The project uses [FastAPI](https://fastapi.tiangolo.com) with [uvicorn](https://www.uvicorn.org) to serve the model inference API.

For deployment within Docker, [gunicorn](https://gunicorn.org) is used as an application server. Find more details here: [FastAPI with Gunicorn and Uvicorn](https://fastapi.tiangolo.com/deployment/server-workers/).

Expose the inference API via:

    `cd pibloom_api/`
    `poetry run uvicorn pibloom.app:app --host 0.0.0.0 --port 5000 --reload`

The API will be exposed to `host='0.0.0.0' (all network interfaces), port=5000`.

<br>

**Local setup with Docker**

To run the API docker image, first build via:

    `cd pibloom_api/`
    `docker build -t pibloom_api .`

Then run the image via:

    `cd pibloom_api/`
    `docker run -it -p 5000:5000 pibloom_api`

<br>

----------------

<br>

**Testing**

Testing is done using [pytest](https://docs.pytest.org/) and run via

    `cd pibloom_api/`
    `poetry run pytest`

<br>

----------------

<br>

### 2. piBLOOM web app

<br>

The web application is build using [Vue.js](https://vuejs.org/). To customize configuration see [Vite Configuration Reference](https://vitejs.dev/config/). Using Docker, the web app files will be served with [expressjs](https://expressjs.com) as middleware, an unopinionated, minimalist web framework for *Node.js*.

Before starting, make sure to update your `.env` file with the correct API url and port, as per [./pibloom_web/.env.example](./pibloom_web/.env.example).

<br>

**Local setup without Docker**

To install dependencies, run:

    `cd pibloom_web/`
    `npm install`

Run the web application in development mode with hot-reloading via:

    `cd pibloom_web/`
    `npm run dev`

Lint with [ESLint](https://eslint.org/)

    `cd pibloom_web/`
    `npm run lint`

Compile and minify for production:

    `cd pibloom_web/`
    `npm run build`

<br>

Running above setup is recommended for simple frontend development, as the middleware is not started for API communication. To start the web app including the *expressjs* middleware, run:

    `cd pibloom_web/`
    `npm run start`

<br>

**Local setup with Docker**

To run the web app docker image, first build via:

    `cd pibloom_web/`
    `docker build -t pibloom_web .`

Then run the image via:

    `cd pibloom_web/`
    `docker run -itd -p 8080:8080 pibloom_web`

**2.2 Testing**

- None

<br>

----------------
----------------

<br>

*Powered by*

<img src="./pibloom_web/src/assets/bloom.png" alt="BLOOM model logo" height="100"/>     <img src="./pibloom_web/src/assets/raspberrypi.svg" alt="raspberry pi logo" height="100"/>

<br>

## TODOs

✅ add web app backend 

✅ update pytest for FastAPI

✅ add docker compose documentation

✅ add expressjs as middleware for web app - API communication

✅ pass number of workers from docker compose to api docker file

✅ add corse policy

✅ utilize custom docker network

✅ add nginx for web app serving in prod

✅ minimize api docker image - Note: further optimization highly beneficial

✅ optimize model

☐ add Kubernetes deployment

☐ review nginx configuration

☐ review corse policy