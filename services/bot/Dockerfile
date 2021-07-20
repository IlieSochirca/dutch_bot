FROM python:3.8.3-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN mkdir -p /srv/dutch_bot/bot/
WORKDIR /srv/dutch_bot

ADD src/requirements.txt bot/requirements.txt
RUN pip3 install -r bot/requirements.txt

COPY src/. bot/.

EXPOSE 8080

#CMD uvicorn main:application --host 0.0.0.0 --port $PORT --reload