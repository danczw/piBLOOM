# provide a common stage for the poetry and runtime stages
FROM python:3-slim as python
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=true
WORKDIR /app

# install Poetry, Python application and dependencies in virtual env
FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
COPY . ./
RUN poetry install --no-interaction --no-ansi -vvv

# builds final Docker Image by copying and configuring virtual env from poetry stage
FROM python as runtime
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=poetry /app /app
WORKDIR /app
CMD [ "python", "./pibloom/app.py" ]