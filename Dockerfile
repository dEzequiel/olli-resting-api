FROM python:3.8-slim

LABEL description="API based in Ollivanders Shop"
LABEL maintainer="Ezequiel De La Rosa - erosario@cifpfbmoll.eu"

RUN apt-get update -y

EXPOSE 5000/udp
EXPOSE 5000/tcp

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT flask run --host=0.0.0.0 --port=5000

# --------------------------------- DEBUGGING ---------------------------------------- #

# This instruction will start the container with a Bash session
# docker run --name olli --rm -i -t ollivanders:latest bash

# With the container running, inside another CLI session you can access the container bash via:
# docker exec -it olli bash
