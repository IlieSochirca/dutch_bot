FROM python:3.8.3-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN mkdir -p /srv/dutch_bot/backend/
WORKDIR /srv/dutch_bot

ADD src/requirements.txt backend/requirements.txt
RUN pip3 install -r backend/requirements.txt

COPY src/. backend/.

EXPOSE 8081

#CMD alembic upgrade head && uvicorn main:application --host 0.0.0.0 --port $PORT --reload