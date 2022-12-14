# pull official base image
FROM python:3.9.6-alpine

# set work directory
RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install gettext dependencies
RUN apk add gettext

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt  /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/
