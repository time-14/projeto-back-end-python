FROM python:3.11

# Não utilizar arquivos .pyc na construção da imagem/container
ENV PYTHONDONTWRITEBYTECODE 1

# Os logs de erro não se perdem entre a aplicação e o container
ENV PYTHONUNBUFFERED 1

WORKDIR /django_app

# COPY . .
COPY . /django_app/

RUN pip install -U pip
RUN pip install -r requirements.txt