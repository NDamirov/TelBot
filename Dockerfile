FROM python:3

WORKDIR /usr/src/app

RUN pip install aiogram

COPY main.py /usr/src/app