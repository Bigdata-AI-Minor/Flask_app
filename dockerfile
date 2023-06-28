# syntax=docker/dockerfile:1

# Use an official ubuntu runtime as a parent image
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

# Set the working directory to /app
WORKDIR /FLASK_APP

# install python and pip
RUN apt-get update && apt-get install -y python3.9 python3-pip

# copy requirements
COPY requirements.txt .

# run requirements
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=manage.py
ENV FLASK_ENV=env

RUN chmod +x /FLASK_APP/entrypoint.sh

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]