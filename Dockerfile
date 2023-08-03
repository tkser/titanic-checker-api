FROM python:3.11

WORKDIR /usr/src/tca

COPY ./app ./app
COPY ./data ./data

COPY pyproject.toml poetry.lock README.md ./

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

CMD [ "poetry", "run", "start" ]