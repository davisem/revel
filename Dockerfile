FROM ubuntu:16.04

RUN apt-get update -y && apt-get install
RUN apt-get install -y python-dev python-pip

ADD . /app/
ENV HOME /app/
WORKDIR /app/

RUN pip install uwsgi
RUN pip install -r ./requirements.txt

EXPOSE 8000

ENV FLASK_APP /app/app.py

ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:8000", "--module", "app:__main__", "--processes", "1", "--threads", "8"]


pip freeze > requirements.txt
docker up
docker run -d
