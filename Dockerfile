#Pull base image
FROM python:3.11.1

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#set work directory
WORKDIR /drfecom

#install dependencies
COPY Pipfile Pipfile.lock /drfecom/
RUN pip install pipenv && pipenv install --system

#copy project
COPY . /drfecom/
