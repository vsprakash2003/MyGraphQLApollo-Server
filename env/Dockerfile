FROM python:3.7-alpine

RUN apk update \
  && apk add --update sqlite\
  build-base

RUN mkdir -p /opt/Myapps/GraphQL-App
WORKDIR /opt/Myapps/GraphQL-App

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./gunicorn_config.py .
RUN pip install gunicorn

ADD . /opt/Myapps/GraphQL-App
EXPOSE 5000
CMD [ "gunicorn", "--config", "gunicorn_config.py", "app:app" ]