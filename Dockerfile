FROM python:3.7
MAINTAINER Gellért Peresztegi-Nagy

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -disabled-login user
USER user
