# piBLOOM - Raspberry Pi based BLOOM model serving

**A web application for serving the BLOOM model via a Raspberry Pi cluster.**

The **BLOOM model**, developed by [BigScience](https://bigscience.huggingface.co) is a transformer based autoregressive Large Language Model (LLM). It is trained to continue text from a prompt on vast amounts of text data using industrial-scale computational resources. As such, it is able to output coherent text in 46 languages and 13 programming languages that is hardly distinguishable from text written by humans. The model is available for download from the [HuggingFace repository](https://huggingface.co/bigscience/bloom), including detailed [model documentation](https://huggingface.co/docs/transformers/model_doc/bloom).

<br>

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
    │  │  ├─ app.py                     # API entry point
    │  │  ├─ model.py                   # model class
    │  │  └─ __init__.py
    │  ├─ poetry.lock
    │  ├─ pyproject.toml
    │  └─ tests                         # API testing
    │     ├─ test_pibloom.py
    │     └─ __init__.py
    ├─ pibloom_web                      # Web application for serving the BLOOM model
    │  ├─ .eslintrc.cjs
    │  ├─ .gitignore
    │  ├─ index.html
    │  ├─ package-lock.json
    │  ├─ package.json
    │  ├─ public
    │  │  └─ favicon.ico
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
    │  │  ├─ router
    │  │  │  └─ index.js
    │  │  └─ views
    │  │     ├─ AboutView.vue           # About page
    │  │     └─ HomeView.vue            # Main page
    │  └─ vite.config.js
    └─ README.md

<br>

----------------

<br>

## 1. piBLOOM API server

### 1.1 Setup

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

The project uses [Flask](https://flask.palletsprojects.com/) to serve the model inference API.

Expose the inference API via:

    `cd pibloom_api/`
    `poetry run flask --app pibloom/app.py run`

The API will be exposed to `host='0.0.0.0', port=5000` by default.

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

### 1.2 Testing

Testing is done using [pytest](https://docs.pytest.org/) and run via

    `cd pibloom_api/`
    `poetry run pytest`

<br>

----------------

<br>

## 2. piBLOOM web app

### 2.1 Setup

The web application is build using [Vue.js](https://vuejs.org/). To customize configuration see [Vite Configuration Reference](https://vitejs.dev/config/).

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

### 2.2 Testing

todo
