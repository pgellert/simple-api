FROM python:3.7
MAINTAINER Gellért Peresztegi-Nagy

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -disabled-login user
USER user

CMD heroku run web python manage.py makemigrations
CMD heroku run web python manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:$PORT
