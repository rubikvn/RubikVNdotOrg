# Following the tutorial from https://wsvincent.com/django-docker-postgresql/

# Pull base image
FROM python:3.6-slim
SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get install -y \
    libffi-dev \
    libssl-dev \
    curl \
    build-essential \
    default-libmysqlclient-dev \
    libxml2-dev \
    net-tools \
    iputils-ping \
    vim \
    gcc

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV RBVN_DEVELOPING true

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /code/Pipfile
RUN pipenv install --system --skip-lock

# Copy project
COPY . /code/
