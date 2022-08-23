# piBLOOM - Raspberry Pi based BLOOM model serving

**A web application for serving the BLOOM model via a Raspberry Pi cluster.**

The **BLOOM model**, developed by [BigScience](https://bigscience.huggingface.co) is a transformer based autoregressive Large Language Model (LLM). It is trained to continue text from a prompt on vast amounts of text data using industrial-scale computational resources. As such, it is able to output coherent text in 46 languages and 13 programming languages that is hardly distinguishable from text written by humans. The model is available for download from the [HuggingFace repository](https://huggingface.co/bigscience/bloom), including detailed [model documentation](https://huggingface.co/docs/transformers/model_doc/bloom).

Goal of the project is to serve a simple web app which allows to "chat" with the BLOOM model of a small [Raspberry Pi](https://www.raspberrypi.org) cluster of approximately 2-4 [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/).

<br>

----------------
----------------

<br>

## Project Structure

<br>

    piBLOOM
    ├─ .gitignore
    ├─ LICENSE
    ├─ pibloom_api                      # API for serving the BLOOM model
    │  ├─ Dockerfile
    │  ├─ pibloom
    │  │  ├─ app.py                     # - API entry point
    │  │  ├─ model.py                   # - Model class
    │  │  └─ __init__.py
    │  ├─ poetry.lock                   # - API dependencies
    │  ├─ pyproject.toml
    │  └─ tests                         # - API testing
    │     ├─ test_pibloom.py
    │     └─ __init__.py
    ├─ pibloom_web                      # Web application for serving the BLOOM model
    │  ├─ .eslintrc.cjs
    │  ├─ .gitignore
    │  ├─ index.html
    │  ├─ package-lock.json             # - Web application dependencies
    │  ├─ package.json
    │  ├─ public
    │  │  └─ [...]
    │  ├─ src
    │  │  ├─ App.vue
    │  │  ├─ assets
    │  │  │  ├─ base.css
    │  │  │  ├─ bloom.png
    │  │  │  ├─ main.css
    │  │  │  └─ raspberrypi.svg
    │  │  ├─ components
    │  │  │  └─ HelloWorld.vue
    │  │  ├─ main.js
    │  │  ├─ router                     # - Web application site routing
    │  │  │  └─ index.js
    │  │  └─ views
    │  │     ├─ AboutView.vue           # - About view
    │  │     └─ HomeView.vue            # - Main view
    │  └─ vite.config.js
    └─ README.md

The API and web application can be served using [Docker](https://www.docker.com), utilizing the `docker-compose.yml` [file](./docker-compose.yml).

Simply install Docker and build the images via:

    `docker-compose.yml`

Then start the container using:

    `docker-compose up`

Alternatively, the API and web application can be served individually (e.g. for development purposes) as per the two steps below.

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

    `poetry install`

<br>

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
    `poetry run docker build -t pibloom_api .`

Then run the image via:

    `cd pibloom_api/`
    `poetry run docker run -it -p 5000:5000 pibloom_api`

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

The web application is build using [Vue.js](https://vuejs.org/). To customize configuration see [Vite Configuration Reference](https://vitejs.dev/config/). Using Docker, the web app files will be served with [NGIИX](https://www.nginx.com), an open source web server framework.

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

**Local setup with Docker**

To run the web app docker image, first build via:

    `cd pibloom_web/`
    `docker build -t pibloom_web .`

Then run the image via:

    `cd pibloom_web/`
    `docker run -it -p 8080:80 pibloom_web`

**2.2 Testing**

todo

<br>

----------------
----------------

<br>

*Powered by*

<img src="./pibloom_web/src/assets/bloom.png" alt="BLOOM model logo" height="100"/>     <img src="./pibloom_web/src/assets/raspberrypi.svg" alt="raspberry pi logo" height="100"/>

<br>

## TODOs

[x]  update pytest for FastAPI
[]  add web app tests
[x]  add docker compose documentation
[]  add docker network for web app to api communication
[]  pass number of workers from docker compose to api docker file
[x] add corse policy
[]  review corse policy
[]  minimize api docker image
[]  optimize model
