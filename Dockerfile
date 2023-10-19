FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/backend

COPY requirements.txt /app/backend/

RUN pip install -r requirements.txt

COPY . /app/backend/

EXPOSE 8000