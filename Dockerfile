FROM python:3.13.0b1-slim

WORKDIR /etc/ZyraSync

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /etc/ZyraSync/requirements.txt

COPY runserver.py /etc/ZyraSync/runserver.py

COPY ZyraSync/ /etc/ZyraSync/ZyraSync/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt
