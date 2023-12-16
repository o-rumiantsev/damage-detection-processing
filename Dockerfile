FROM python:3.11-slim

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8000
