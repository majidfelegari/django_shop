FROM python:3.10-slim-buster

LABEL maintainer="f.majid1377@gmail.com"

ENV PYTHONUNBUFFERD=1

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./core .