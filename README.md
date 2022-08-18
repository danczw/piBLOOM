# piBLOOM - Raspberry Pi based BLOOM model serving

**A web application for serving the BLOOM model via a Raspberry Pi cluster.**

The **BLOOM model**, developed by [BigScience](https://bigscience.huggingface.co) is a transformer based autoregressive Large Language Model (LLM). It is trained to continue text from a prompt on vast amounts of text data using industrial-scale computational resources. As such, it is able to output coherent text in 46 languages and 13 programming languages that is hardly distinguishable from text written by humans. The model is available for download from the [HuggingFace repository](https://huggingface.co/bigscience/bloom), including detailed [model documentation](https://huggingface.co/docs/transformers/model_doc/bloom).

<br>

----------------

<br>

## Project Structure

    .
    ├─ pibloom_api                  # model inference API server
    │  ├─ pibloom
    │  │  ├─ app.py
    │  │  ├─ model.py
    │  │  └─ __init__.py
    │  ├─ poetry.lock
    │  ├─ pyproject.toml
    │  └─ tests
    │     ├─ test_pibloom.py
    │     └─ __init__.py
    ├─ README.md
    ├─ .gitignore
    └─ LICENSE

<br>

----------------

<br>

## Setup

The project uses [Poetry](https://python-poetry.org) to manage the project dependencies. Install dependencies via:

    `poetry install`

The project uses [Flask](https://flask.palletsprojects.com/) to serve the model inference API as well as the web app.

Expose the inference API via:

    `poetry run flask --app pibloom/app.py run`

The API will be exposed to `host='127.0.0.1', port=5000` by default

<br>

----------------

<br>

## Testing

Testing is done using [pytest](https://docs.pytest.org/) and run via

    `poetry run pytest`
